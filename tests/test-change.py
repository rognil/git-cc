__author__ = 'nilstrog'

import unittest
import os

from os.path import join
from cctogitlogger import CcToGitLogger
from constants import GitCcConstants


class DirectoryChangeTest(unittest.TestCase):

    def test_change(self):


        path = os.getcwd().split(GitCcConstants.file_separator())
        CcToGitLogger(join(GitCcConstants.file_separator().join(path),
                         GitCcConstants.conf_dir(), GitCcConstants.logger_conf_name()))

        _configuration = __import__('configuration')
        _cache = __import__('cache')
        _change_set = __import__('changeset')

        base_dir = GitCcConstants.file_separator().join('.')
        config = _configuration.ConfigParser()
        config.init(base_dir)
        cache = _cache.NoCache()

        line = 'checkindirectory version|20110427.150714|user|/clearcase/proj/dir/util|/main/proj/subproj/2|Added element "mkdefs.sparcv9".'
        split = line.split(GitCcConstants.attribute_delimiter())
        cs = _change_set.Change(cache, config, None, None, split, '')
        print 'Branch %s' % cs.branch
        self.assertTrue(cs.branch == 'main_proj_subproj')

    def test_ignore_to_compl_change(self):

        change = 'cleartool get -to /home/nanne/proj/Tools/Util/inc@@/main/axe/1/Ndb/main/1/NdbApi_V1.H ' \
                 '/clearcase/proj/Tools/Util/inc@@/main/axe/1/Ndb/main/1/NdbApi_V1.H@@/main/1'
        print 'Occurenses: %s' % change.count('@@')
        self.assertTrue(change.count('@@') == 3)

if __name__ == "__main__":
    unittest.main()
