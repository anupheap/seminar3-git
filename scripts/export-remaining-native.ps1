param([string]$ProjectRoot = (Split-Path $PSScriptRoot -Parent))
$ErrorActionPreference = 'Stop'
$app = New-Object -ComObject PowerPoint.Application
try {
    foreach ($spec in @(@{Name='Seminar';Lecture=2;Start=19;End=30},@{Name='Presentation2';Lecture=3;Start=1;End=12},@{Name='Lecture5';Lecture=5;Start=1;End=11})) {
        $output = Join-Path $ProjectRoot ".cache/lecture$($spec.Lecture)-native"
        New-Item -ItemType Directory -Force -Path $output | Out-Null
        $deck = $app.Presentations.Open((Join-Path $ProjectRoot "public/sources/powerpoint/$($spec.Name).pptx"), -1, 0, 0)
        try {
            $slides = @()
            for ($number=$spec.Start; $number -le $spec.End; $number++) {
                $slide=$deck.Slides.Item($number)
                $items=@()
                foreach ($shape in $slide.Shapes) {
                    $filename='{0:D2}-{1}.svg' -f $number,$shape.Id
                    $shape.Export((Join-Path $output $filename),6)
                    $items += [ordered]@{id=[int]$shape.Id;name=$shape.Name;file=$filename;bounds=@(([double]$shape.Left*4/3),([double]$shape.Top*4/3),([double]$shape.Width*4/3),([double]$shape.Height*4/3))}
                }
                $rgb=[int]$slide.Background.Fill.ForeColor.RGB
                $color='#{0:X2}{1:X2}{2:X2}' -f ($rgb-band 255),(($rgb-shr 8)-band 255),(($rgb-shr 16)-band 255)
                $slides += [ordered]@{number=$number;backgroundColor=$color;objects=$items}
                Write-Output "Lecture $($spec.Lecture), original slide $number exported."
            }
            [ordered]@{deck=$spec.Name;lecture=$spec.Lecture;width=([double]$deck.PageSetup.SlideWidth*4/3);height=([double]$deck.PageSetup.SlideHeight*4/3);slides=$slides} | ConvertTo-Json -Depth 15 | Set-Content -LiteralPath (Join-Path $output 'manifest.json') -Encoding utf8
        } finally {$deck.Close()}
    }
} finally {[Runtime.InteropServices.Marshal]::ReleaseComObject($app)|Out-Null}
