#!/usr/bin/env python3

import urllib.request
import terminalsize

class Downloader:
    "Download file and show progress in command line"

    def __init__(self):
        self.fileName = ''


    def _reportDownload(self, blocksDownload, blockSize, fileSize):
        'Print progress of the actual download'
        sizeDownloaded = int(blockSize * blocksDownload / 1024)
        totalSize = int(fileSize / 1024)
        percentDown = 0.0

        if sizeDownloaded != 0:
            percentDown = sizeDownloaded / totalSize

        term_width = terminalsize.get_terminal_size()[0]

        if not sizeDownloaded < totalSize:
            sizeDownloaded = totalSize

        leftMsg = (self.fileName + '  [')
        rightMsg = '] ' + str(sizeDownloaded) + ' / ' + str(totalSize) + ' KB'
        leftSize = len(leftMsg)
        consoleSpace = term_width - (leftSize + 20) # plus 16 to have a reserve from end with right message for showing size
        showNumSharps = int(consoleSpace * percentDown)

        print(leftMsg.ljust(showNumSharps + leftSize, '#').ljust(consoleSpace + leftSize) + rightMsg, end='\r')

        if not sizeDownloaded < totalSize:
            print('')

    def downloadFile(self, link, name=""):
        'Download file and register for creating graphical progress'
        if not name:
            self.fileName = link.split('/')[-1]
        else:
            self.fileName = name

        (filename, headers) = urllib.request.urlretrieve(link, reporthook=self._reportDownload)
        return filename

