from __future__ import division
import numpy as np
from glob import glob
import os
import scipy.misc
import random


class humanbody_loader(object):
    def __init__(self,
                 dataset_dir,
                 split,
                 img_height=256,
                 img_width=256,
                 seq_length=5,
                 samplenum = 100,
                 mode = 1):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #static_frames_file = dir_path + '/static_frames.txt'
        test_scene_file = dir_path + '/test_scenes_' + split + '.txt'
        # with open(test_scene_file, 'r') as f:
        #     test_scenes = f.readlines()
        #self.test_scenes = [t[:-1] for t in test_scenes]
        self.dataset_dir = dataset_dir
        self.samplenum = samplenum;
        self.mode = mode
        self.img_height = img_height
        self.img_width = img_width
        self.seq_length = seq_length
        self.quality_list = ['hdImgs', 'vgaImgs']
        self.cam_ids = []
        self.date_list = ['141216_pose1', '141217_pose1', '141217_pose2',
                          '141217_pose3', '141217_pose4', '141217_pose5','141217_pose6']
        for i in range(20)
            for j in range(20)
                frame_id = '%.2d' % i
                moduel_id = '%.2d' % j
                self.cam_ids.append(frame_id + '_' + moduel_id)

        #self.collect_static_frames(static_frames_file)
        self.collect_train_frames()



    def collect_train_frames(self):
        all_samples = []
        for date in self.date_list:
            date_dir = self.dataset_dir + date + '/' + self.quality_list[self.mode] + '/'
            drive_set = os.listdir(date_dir)
            addlist = []
            for dr in drive_set:
                drive_dir = os.path.join(date_dir, dr)
                if len(os.listdir(date_dir)) > 0:
                        for i in range(self.samplenum)
                            addlist.append(random.randint(0, len(os.listdir(drive_dir))))
                    break

            for i in range(self.samplenum)
                all_frames = []
                for dr in drive_set:
                    drive_dir = os.path.join(date_dir, dr)
                    if len(os.listdir(date_dir)) > 0:
                            img_idx = '%.8d' % addlist[i]
                            all_frames.append( date + '' + dr + '' + img_idx)
                all_samples.append(all_frames)


                        # for cam in self.cam_ids:
                        #     img_dir = os.path.join(drive_dir, 'image_' + cam, 'data')
                        #     N = len(glob(img_dir + '/*.png'))
                        #     for n in range(N):
                        #         frame_id = '%.10d' % n
                        #         all_frames.append(dr + ' ' + cam + ' ' + frame_id)

        # for s in self.static_frames:
        #     try:
        #         all_frames.remove(s)
        #         # print('removed static frame from training: %s' % s)
        #     except:
        #         pass

        self.all_samples = all_samples
        self.num_train = len(self.all_samples)