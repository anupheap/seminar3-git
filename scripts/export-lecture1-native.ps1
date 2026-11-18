param([string]$ProjectRoot = (Split-Path $PSScriptRoot -Parent))

# Export original objects as native SVG, never as slide screenshots.
# Presentations are opened read-only and are never saved.
$ErrorActionPreference = 'Stop'
$output = Join-Path $ProjectRoot '.cache/lecture1-native'
New-Item -ItemType Directory -Force -Path $output | Out-Null
$app = New-Object -ComObject PowerPoint.Application
$deck = $app.Presentations.Open((Join-Path $ProjectRoot 'public/sources/powerpoint/Seminar.pptx'), -1, 0, 0)
try {
    $slides = @()
    for ($number = 1; $number -le 17; $number++) {
        $items = @()
        foreach ($shape in $deck.Slides.Item($number).Shapes) {
            if ($number -eq 3 -and $shape.Id -in @(1499, 1501)) { continue }
            $filename = '{0:D2}-{1}.svg' -f $number, $shape.Id
            $shape.Export((Join-Path $output $filename), 6)
            $items += [ordered]@{
                id = [int]$shape.Id; name = $shape.Name; file = $filename
                bounds = @(([double]$shape.Left * 4/3), ([double]$shape.Top * 4/3), ([double]$shape.Width * 4/3), ([double]$shape.Height * 4/3))
            }
        }
        $slides += [ordered]@{ number = $number; objects = $items }
        Write-Output "Lecture 1: native objects exported for original slide $number."
    }
    $slides | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $output 'manifest.json') -Encoding utf8
} finally {
    $deck.Close()
    [Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
