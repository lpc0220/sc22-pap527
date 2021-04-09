from __future__ import absolute_import, division, print_function, unicode_literals

import csv
import collections
import io
import os.path


from absl import app
from absl import flags

from tensorflow.compat.v1 import logging
logging.set_verbosity(logging.INFO)

"""
The script must be run in current directory.
"""


FLAGS = flags.FLAGS

flags.DEFINE_string('dataset_path', 'data_sets', '')
flags.DEFINE_integer('encoder_len', 64, '')
flags.DEFINE_integer('decoder_len', 16, '')


#_TRACES = ['rsrch_0', 'rsrch_1', 'rsrch_2', 'src1_0',
#           'src1_1', 'src1_2', 'src2_0', 'src2_1', 'src2_2',
#           'stg_0', 'stg_1', 'ts_0', 'usr_0', 'usr_1',
#           'usr_2', 'wdev_0', 'wdev_1', 'wdev_2',
#           'wdev_3', 'web_0', 'web_1', 'web_2', 'web_3']
_TRACES = ['src2_1', 'src2_2', 'wdev_0', 'wdev_1', 'wdev_2', 'wdev_3',
            'web_1', 'web_3']

def run_cmd(cmd):
  logging.info('%s', cmd)
  os.system(cmd)


def basic_command():
  cmd = 'bazel-bin/feature_to_examples '
  cmd += '--encoder_len={} '.format(FLAGS.encoder_len)
  cmd += '--decoder_len={} '.format(FLAGS.decoder_len)
  return cmd


def generate_cmd(filename, trace, suffix):
  cmd = basic_command()
  data_path = FLAGS.dataset_path + '/' + 'data_set_' + trace + '_' + suffix
  data_path += '/' + filename
  cmd += '--dataset_path {} '.format(data_path)
  return cmd


def generate_examples_file_for(trace):
  cmd = generate_cmd('norm_trace_0.csv', trace, 'pred')
  run_cmd(cmd)

  cmd = generate_cmd('eval_norm_trace_0.csv', trace, 'pred')
  run_cmd(cmd)

  cmd = generate_cmd('norm_trace_0.csv', trace, 'class')
  run_cmd(cmd)

  cmd = generate_cmd('eval_norm_trace_0.csv', trace, 'class')
  run_cmd(cmd)




def main(argv=()):
  del argv  # Unused

  for trace in _TRACES:
    generate_examples_file_for(trace)


if __name__ == '__main__':
  app.run(main)
