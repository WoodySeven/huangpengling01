#!/usr/bin/env python
#-*- coding utf-8 -*-


def transferScale(sourceNum:int, targetScale):
 # if not isinstance(sourceNum, int):
   # raise TypeError('sourceNum type must be int and 10 scale.')

  if not targetScale in [2, 8, 10, 16]:
    raise TypeError('targetScale must be one of [2, 8, 10, 16].')

  numberScaleMap_16 = {
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f'
  }

  targetNumArr = []

  if (sourceNum < targetScale):
    if (targetScale == 16 and numberScaleMap_16.__contains__(sourceNum)):
      targetNumArr.insert(0, numberScaleMap_16.get(sourceNum))
    else:
      targetNumArr.insert(0, str(sourceNum))
  else:
    while (sourceNum // targetScale > 0):
      if (targetScale == 16 and numberScaleMap_16.__contains__(sourceNum % targetScale)):
        targetNumArr.insert(0, numberScaleMap_16.get(sourceNum % targetScale))
      else:
        targetNumArr.insert(0, str(sourceNum % targetScale))

      sourceNum = sourceNum // targetScale

      if (sourceNum // targetScale == 0):
        if (targetScale == 16 and numberScaleMap_16.__contains__(sourceNum)):
          targetNumArr.insert(0, numberScaleMap_16.get(sourceNum))
        else:
          targetNumArr.insert(0, str(sourceNum))

  if (targetScale == 2):
    targetNumArr.insert(0, '0b')
  elif (targetScale == 8):
    targetNumArr.insert(0, '0')
  elif (targetScale == 16):
    targetNumArr.insert(0, '0x')

  return ''.join(targetNumArr)

if __name__ == "__main__":
 print(transferScale(13, 16))

