param([string]$ProjectRoot = (Split-Path $PSScriptRoot -Parent))

# Read-only layout measurements. The preserved presentation is never saved.
$ErrorActionPreference = 'Stop'
$app = New-Object -ComObject PowerPoint.Application
$deck = $app.Presentations.Open((Join-Path $ProjectRoot 'public/sources/powerpoint/Seminar.pptx'), -1, 0, 0)
function Read-Shape($shape) {
    $result = [ordered]@{ id = [int]$shape.Id; name = $shape.Name }
    if ($shape.Type -eq 6) {
        $children = @()
        foreach ($child in $shape.GroupItems) { $children += Read-Shape $child }
        $result.children = $children
    }
    if ($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1) {
        $range = $shape.TextFrame.TextRange
        $result.text = $range.Text
        $result.bounds = @([double]$range.BoundLeft, [double]$range.BoundTop, [double]$range.BoundWidth, [double]$range.BoundHeight)
        $lines = @()
        for ($index = 1; $index -le $range.Lines().Count; $index++) {
            $line = $range.Lines($index, 1)
            $runs = @()
            for ($runIndex = 1; $runIndex -le $line.Runs().Count; $runIndex++) {
                $run = $line.Runs($runIndex, 1)
                $runs += [ordered]@{
                    text = $run.Text; start = [int]$run.Start; length = [int]$run.Length
                    bounds = @([double]$run.BoundLeft, [double]$run.BoundTop, [double]$run.BoundWidth, [double]$run.BoundHeight)
                    font = $run.Font.Name; size = [double]$run.Font.Size
                    bold = ($run.Font.Bold -eq -1); italic = ($run.Font.Italic -eq -1)
                    underline = ($run.Font.Underline -eq -1)
                    color = [int]$run.Font.Color.RGB
                    baseline = [double]$run.Font.BaselineOffset
                }
            }
            $lines += [ordered]@{
                text = $line.Text; start = [int]$line.Start; length = [int]$line.Length
                bounds = @([double]$line.BoundLeft, [double]$line.BoundTop, [double]$line.BoundWidth, [double]$line.BoundHeight)
                runs = $runs
                bullet = [ordered]@{ type = [int]$line.ParagraphFormat.Bullet.Type; character = [int]$line.ParagraphFormat.Bullet.Character; font = $line.ParagraphFormat.Bullet.Font.Name }
            }
        }
        $result.lines = $lines
    }
    return $result
}
try {
    $slides = @()
    for ($number = 1; $number -le 17; $number++) {
        $shapes = @()
        foreach ($shape in $deck.Slides.Item($number).Shapes) { $shapes += Read-Shape $shape }
        $slides += [ordered]@{ number = $number; shapes = $shapes }
    }
    $slides | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $ProjectRoot 'sources/lecture1-layout.json') -Encoding utf8
    Write-Output 'Read original layout measurements for Lecture 1 (17 slides).'
} finally {
    $deck.Close()
    [Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
