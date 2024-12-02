# running the inference script with different seeds each time

import os

for i in range (500):
    outdir_name_='output_{}'.format(i)
    os.system('mkdir samples/03_fwd_facing_masks_custom_trained_fwd_facing_maps/tick_160/{}'.format(outdir_name_))
    os.system('python generate_image.py --network pretrained/03_custom_fwd_facing_masks_fwd_facing_maps/network-snapshot-000640.pkl --dpath test_sets/elevation_maps/maps_fwd_facing --mpath test_sets/elevation_maps/mask_fwd_facing --outdir samples/03_fwd_facing_masks_custom_trained_fwd_facing_maps/tick_160/{} --resolution 256'.format(outdir_name_))