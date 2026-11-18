param([string]$ProjectRoot=(Split-Path $PSScriptRoot -Parent))
$ErrorActionPreference='Stop'
$map=Get-Content -Raw (Join-Path $ProjectRoot '.cache/native-inherited-map.json') | ConvertFrom-Json
$app=New-Object -ComObject PowerPoint.Application
try {
 foreach($spec in @(@{Name='Seminar';Lecture=2},@{Name='Presentation2';Lecture=3},@{Name='Lecture5';Lecture=5})){
  $output=Join-Path $ProjectRoot ".cache/lecture$($spec.Lecture)-native"
  $manifest=Get-Content -Raw (Join-Path $output 'manifest.json')|ConvertFrom-Json
  $deck=$app.Presentations.Open((Join-Path $ProjectRoot "public/sources/powerpoint/$($spec.Name).pptx"),-1,0,0)
  try{
   foreach($page in $manifest.slides){
    $slide=$deck.Slides.Item($page.number);$items=@()
    foreach($entry in $map.($spec.Name).([string]$page.number)){
     $collection=if($entry.level-eq'layout'){$slide.CustomLayout.Shapes}else{$slide.Master.Shapes}
     $shape=$null
     foreach($candidate in $collection){if($candidate.Id-eq$entry.shapeId){$shape=$candidate;break}}
     if($null-eq$shape){throw "Inherited shape missing: $($spec.Name) $($page.number) $($entry.shapeId)"}
     $filename="$($page.number)-$($entry.level)-$($entry.shapeId).svg"
     $shape.Export((Join-Path $output $filename),6)
     $id=if($entry.level-eq'layout'){-200000-$entry.shapeId}else{-100000-$entry.shapeId}
     $items += [ordered]@{id=$id;shapeId=$entry.shapeId;part=$entry.part;name=$shape.Name;file=$filename;bounds=@(([double]$shape.Left*4/3),([double]$shape.Top*4/3),([double]$shape.Width*4/3),([double]$shape.Height*4/3))}
    }
    $page|Add-Member -NotePropertyName inherited -NotePropertyValue $items -Force
   }
   $manifest|ConvertTo-Json -Depth 20|Set-Content -LiteralPath (Join-Path $output 'manifest.json') -Encoding utf8
   Write-Output "Lecture $($spec.Lecture): original inherited layout objects exported."
  }finally{$deck.Close()}
 }
}finally{[Runtime.InteropServices.Marshal]::ReleaseComObject($app)|Out-Null}
