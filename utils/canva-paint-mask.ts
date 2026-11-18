/** Replay Canva's original brush mask on the existing picture element. */
export function createCanvaPaintMask(image:HTMLImageElement,src:string,duration:number){
 const video=document.createElement('video')
 video.muted=true;video.playsInline=true;video.preload='auto';video.src=src
 const canvas=document.createElement('canvas')
 canvas.width=640;canvas.height=360
 const context=canvas.getContext('2d')!
 let frame:number|undefined,version=0,disposed=false
 const mask=(value:string)=>{
  image.style.maskImage=value;image.style.webkitMaskImage=value
  image.style.maskMode='luminance';image.style.maskSize='100% 100%';image.style.maskRepeat='no-repeat'
 }
 const reset=()=>{mask('linear-gradient(transparent,transparent)');image.dataset.canvaPaint='waiting'}
 const draw=()=>{
  if(video.readyState<2)return
  context.drawImage(video,0,0,640,360)
  mask(`url(${canvas.toDataURL('image/png')})`)
  image.dataset.canvaPaint=video.currentTime>=duration/1000-.025?'complete':'playing'
 }
 const pause=()=>{
  version++;video.pause()
  if(frame!==undefined)video.cancelVideoFrameCallback(frame)
  frame=undefined
 }
 const ready=new Promise<void>((resolve,reject)=>{
  video.addEventListener('loadeddata',()=>resolve(),{once:true})
  video.addEventListener('error',()=>reject(new Error(`Canva paint mask failed to load: ${src}`)),{once:true})
  video.addEventListener('abort',()=>{if(disposed)resolve()},{once:true})
 })
 reset();video.load()
 const play=async()=>{
  pause();const run=version;reset();await ready
  if(disposed||run!==version)return
  if(video.currentTime>.001){
   const seeked=new Promise<void>(resolve=>video.addEventListener('seeked',()=>resolve(),{once:true}))
   video.currentTime=0;await seeked
  }
  if(disposed||run!==version)return
  draw()
  const tick=()=>{
   if(disposed||run!==version)return
   draw()
   if(video.currentTime>=duration/1000-.025){video.pause();return}
   frame=video.requestVideoFrameCallback(tick)
  }
  try{await video.play()}catch(error){if(disposed||run!==version)return;throw error}
  if(disposed||run!==version){video.pause();return}
  frame=video.requestVideoFrameCallback(tick)
 }
 const showStatic=()=>{pause();mask('none');image.dataset.canvaPaint='static'}
 const dispose=()=>{disposed=true;pause();video.removeAttribute('src');video.load()}
 return{ready,play,pause,showStatic,dispose}
}
