"""Copy Manim outputs and extract matching posters into public/animations."""
from pathlib import Path
import argparse
import shutil
import av

SCENES={
    'linear_algebra':['ColumnCombination','EliminationGeometry','DependenceAndBasis'],
    'expanded_scenes':['RowIntersection','EliminationPivots','MatrixComposition',
        'GaussJordanInverse','MatrixTranspose','PermutationRows',
        'ColumnSpaceSweep','NullspacePlane','BasisCoordinates'],
}


def publish(media,output):
    output.mkdir(parents=True,exist_ok=True)
    for module,names in SCENES.items():
        for name in names:
            source=media/'videos'/module/'720p30'/f'{name}.mp4'
            if not source.exists():
                raise FileNotFoundError(f'Render this scene first: {source}')
            shutil.copy2(source,output/f'{name}.mp4')
            with av.open(str(source)) as video:
                duration=video.duration/av.time_base
                time=max(0,duration-.8)
                video.seek(int(time*av.time_base))
                frame=next(f for f in video.decode(video=0) if f.time>=time-.05)
                frame.to_image().save(output/f'{name}.jpg',quality=92)
            print(f'{name}: {duration:.1f}s')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--media',type=Path,default=Path('media'))
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'public/animations')
    args=parser.parse_args()
    publish(args.media,args.output)
