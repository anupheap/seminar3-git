param(
    [string]$ProjectRoot = (Split-Path $PSScriptRoot -Parent)
)

# Open the preserved copies read-only, without a presentation window. Never save.
# PowerPoint supplies the original typography, equations, images and shape layers.
$ErrorActionPreference = 'Stop'
$pptApp = New-Object -ComObject PowerPoint.Application
$allDecks = @()
$Decks = @('Seminar', 'Presentation2', 'Lecture5')
try {
    foreach ($deckName in $Decks) {
        $sourcePath = Join-Path $ProjectRoot "public/sources/powerpoint/$deckName.pptx"
        $outputDir = Join-Path $ProjectRoot "public/sources/slides/$deckName"
        New-Item -ItemType Directory -Force $outputDir | Out-Null
        $deck = $pptApp.Presentations.Open($sourcePath, -1, 0, 0)
        try {
            $slides = @()
            for ($slideIndex = 1; $slideIndex -le $deck.Slides.Count; $slideIndex++) {
                $slide = $deck.Slides.Item($slideIndex)
                $prefix = '{0:D2}' -f $slideIndex
                $publicPath = "/sources/slides/$deckName/$prefix"
                $slide.Export((Join-Path $outputDir "$prefix.png"), 'PNG', 1920, 1080)
                $effects = @()
                $targets = @{}
                $stage = 0
                $lastStart = 0.0
                $lastEnd = 0.0
                $sequence = $slide.TimeLine.MainSequence
                for ($effectIndex = 1; $effectIndex -le $sequence.Count; $effectIndex++) {
                    $effect = $sequence.Item($effectIndex)
                    $shape = $effect.Shape
                    $trigger = [int]$effect.Timing.TriggerType
                    $delay = [double]$effect.Timing.TriggerDelayTime
                    if ($trigger -eq 1 -or $trigger -eq 4) {
                        $stage++
                        $lastStart = 0.0
                        $lastEnd = 0.0
                    }
                    $start = $delay
                    if ($trigger -eq 3) { $start += $lastEnd }
                    elseif ($trigger -eq 2) { $start += $lastStart }
                    $duration = [Math]::Max(0.01, [double]$effect.Timing.Duration)
                    $lastStart = $start
                    $lastEnd = $start + $duration
                    $direction = 0
                    try { $direction = [int]$effect.EffectParameters.Direction } catch {}
                    $effects += [ordered]@{
                        index = $effectIndex; shape = [int]$shape.Id
                        type = [int]$effect.EffectType; exit = ($effect.Exit -eq -1)
                        trigger = $trigger; step = $stage
                        delay = [Math]::Round($start, 4); duration = [Math]::Round($duration, 4)
                        direction = $direction
                    }
                    $targets[[int]$shape.Id] = $shape
                }
                # Hide animated shapes only for the static background export.
                $visibility = @{}
                foreach ($shapeId in $targets.Keys) {
                    $visibility[$shapeId] = $targets[$shapeId].Visible
                    $targets[$shapeId].Visible = 0
                }
                $slide.Export((Join-Path $outputDir "$prefix-base.png"), 'PNG', 1920, 1080)
                foreach ($shapeId in $targets.Keys) { $targets[$shapeId].Visible = $visibility[$shapeId] }
                $layers = @()
                foreach ($shapeId in $targets.Keys) {
                    # Duplicate in memory so grouping cannot change the source slide.
                    $layerSlide = $slide.Duplicate().Item(1)
                    try {
                        $target = $null
                        foreach ($candidate in $layerSlide.Shapes) {
                            if ($candidate.Id -eq $shapeId) { $target = $candidate; break }
                        }
                        if ($null -eq $target) { throw "Nested animation target $shapeId on $deckName slide $slideIndex" }
                        $target.Name = "slidev-export-$shapeId"
                        # A transparent slide-size rectangle fixes the export bounds.
                        $frame = $layerSlide.Shapes.AddShape(1, 0, 0, $deck.PageSetup.SlideWidth, $deck.PageSetup.SlideHeight)
                        $frame.Fill.Visible = -1
                        $frame.Fill.Transparency = 1
                        $frame.Line.Visible = 0
                        $frame.ZOrder(1)
                        $names = @($target.Name, $frame.Name)
                        $layerRange = $layerSlide.Shapes.Range($names)
                        $layerName = "$prefix-shape-$shapeId.png"
                        $layerRange.Export((Join-Path $outputDir $layerName), 2, 1440, 810, 1)
                        $layers += [ordered]@{ shape = $shapeId; src = "/sources/slides/$deckName/$layerName" }
                    } finally { $layerSlide.Delete() }
                }
                $slides += [ordered]@{
                    number = $slideIndex; image = "$publicPath.png"
                    background = "$publicPath-base.png"; clicks = $stage
                    effects = @($effects); layers = @($layers)
                }
                Write-Output "$deckName slide $slideIndex exported ($($effects.Count) effects, $stage clicks)"
            }
            $allDecks += [ordered]@{
                id = $deckName; source = "/sources/powerpoint/$deckName.pptx"
                width = [double]$deck.PageSetup.SlideWidth; height = [double]$deck.PageSetup.SlideHeight
                slides = @($slides)
            }
        } finally {
            # Discard only the in-memory visibility/grouping operations.
            $deck.Saved = -1
            $deck.Close()
        }
    }
    $manifestPath = Join-Path $ProjectRoot 'sources/powerpoint.json'
    $allDecks | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $manifestPath -Encoding utf8
} finally {
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pptApp) | Out-Null
}
