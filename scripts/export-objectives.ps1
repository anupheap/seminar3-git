param([string]$ProjectRoot = (Split-Path $PSScriptRoot -Parent))

# Export every original foreground object on Seminar's Learning Objectives slide.
# The original presentation is opened read-only and is never saved.
$ErrorActionPreference = 'Stop'
$sourcePath = Join-Path $ProjectRoot 'public/sources/powerpoint/Seminar.pptx'
$outputDir = Join-Path $ProjectRoot 'public/sources/slides/Seminar/objectives'
New-Item -ItemType Directory -Force $outputDir | Out-Null
$pptApp = New-Object -ComObject PowerPoint.Application
$deck = $null
try {
    $deck = $pptApp.Presentations.Open($sourcePath, -1, 0, 0)
    $slide = $deck.Slides.Item(3)
    $visibility = @{}
    foreach ($shape in $slide.Shapes) {
        $visibility[[int]$shape.Id] = $shape.Visible
        $shape.Visible = 0
    }
    $slide.Export((Join-Path $outputDir 'background.png'), 'PNG', 1920, 1080)
    foreach ($shape in $slide.Shapes) { $shape.Visible = $visibility[[int]$shape.Id] }
    $layers = @()
    foreach ($shape in $slide.Shapes) {
        $shapeId = [int]$shape.Id
        $layerSlide = $slide.Duplicate().Item(1)
        try {
            $target = $null
            foreach ($candidate in $layerSlide.Shapes) {
                if ($candidate.Id -eq $shapeId) { $target = $candidate; break }
            }
            if ($null -eq $target) { throw "Missing objectives shape $shapeId" }
            # Duplicated source shapes can share a name. Range resolves names,
            # so give the selected object a unique name in this disposable copy.
            $target.Name = "objective-export-$shapeId"
            $frame = $layerSlide.Shapes.AddShape(1, 0, 0, $deck.PageSetup.SlideWidth, $deck.PageSetup.SlideHeight)
            $frame.Fill.Visible = -1
            $frame.Fill.Transparency = 1
            $frame.Line.Visible = 0
            $frame.ZOrder(1)
            $range = $layerSlide.Shapes.Range(@($target.Name, $frame.Name))
            $range.Export((Join-Path $outputDir "$shapeId.png"), 2, 1440, 810, 1)
            $label = $shape.Name
            if ($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1) { $label = $shape.TextFrame.TextRange.Text }
            $layers += [ordered]@{
                shape = $shapeId
                src = "/sources/slides/Seminar/objectives/$shapeId.png"
                label = $label
                origin = @(
                    (([double]$shape.Left + [double]$shape.Width / 2) / $deck.PageSetup.SlideWidth * 100),
                    (([double]$shape.Top + [double]$shape.Height / 2) / $deck.PageSetup.SlideHeight * 100)
                )
            }
        } finally { $layerSlide.Delete() }
    }
    [ordered]@{
        background = '/sources/slides/Seminar/objectives/background.png'
        image = '/sources/slides/Seminar/03.png'
        layers = @($layers)
    } | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $ProjectRoot 'sources/learning-objectives.json') -Encoding utf8
    Write-Output "Exported all $($layers.Count) Learning Objectives elements and a clean background."
} finally {
    if ($null -ne $deck) { $deck.Saved = -1; $deck.Close() }
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pptApp) | Out-Null
}
