#!/bin/bash
# resources/scripts/freeCadBackupCleanner.sh

find ./ -regex '.*\.FCStd[0-9]+' -print -delete
find ./ -name '*.FCBak' -print -delete
