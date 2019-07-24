import logging
import unittest

LOG = logging.getLogger(__name__)


class CheckLabels(object):

    def __init__(self, labels):
        self.labels = "quick or express and datapath and not scale"
        self.match_labels = []
        self.skip_labels = []
        self.parse_labels()

    def parse_labels(self):
        label_iter = iter(filter(None, self.labels.split(" ")))
        label_groups = []
        attrib = label_groups
        for label in label_iter:
            if label == "not":
                attrib = self.skip_labels
            elif label == "and":
                attrib = label_groups
            elif label == "or":
                attrib = self.match_labels
            else:
                attrib.append(label)
        if label_groups:
            self.match_labels.append(label_groups)

        self.skip_labels = set(self.skip_labels)

    def has_skip_label(self, testlabels):
        if self.skip_labels:
            common_labels = list(testlabels.intersection(self.skip_labels))
            if common_labels:
                LOG.debug("Test has skip label(s): {}".format(common_labels))
                print ("Test has skip label(s): {}".format(common_labels))
                return True
        return False

    def has_match_label(self, testlabels):
        if self.match_labels:
            for label in self.match_labels:
                if not isinstance(label, list):
                    label = label.split()
                label = set(label)
                if not label.issubset(testlabels):
                    missing_labels = list(label.difference(testlabels))
                    LOG.debug("Test doesn't have label(s): {}".format(missing_labels))
                    print ("Test doesn't have label(s): {}".format(missing_labels))
                    return False
        return True

    def should_run(self, testlabels):
        return (not self.has_skip_label(testlabels)
                and self.has_match_label(testlabels))


class TestCheckLabels(unittest.TestCase):

    def test01():
        labels = "quick or express and datapath and not scale"
        cl = CheckLabels(labels)

        testlabels1 = {'express', 'quick', 'datapath', 'functional'}
        testlabels2 = {'express', 'quick', 'functional'}
        testlabels3 = {'express', 'quick', 'datapath', 'scale'}
        testlabels4 = {'express', 'quick', 'controlpath', 'functional'}

        print "Match Labels: {}".format(cl.skip_labels)
        print "Skip  Labels: {}".format(cl.match_labels)
        for testlabels in [testlabels1, testlabels2, testlabels3, testlabels4]:
            print "-" * 50
            print "TestLabels: {}".format(testlabels)
            skip = cl.has_skip_label(testlabels)
            match = cl.has_match_label(testlabels)
            run = cl.should_run(testlabels)
            print "Skip: {}, Run: {}, Will Run: {}".format(
                skip, match, run)
