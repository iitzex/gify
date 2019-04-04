import glob

import moviepy.editor as mpy

file_list = glob.glob('screenshot/*.png')
# print(file_list)
f = sorted(file_list)

fps = 12
FN = 'tpeflow'
clip = mpy.ImageSequenceClip(f, fps=fps)
clip.write_gif(f'{FN}.gif', fps=fps)

# images = []
# for filename in f:
#     print(f)
#     images.append(imageio.imread(filename))
# imageio.mimsave(gif_name, images, duration=0.05)
