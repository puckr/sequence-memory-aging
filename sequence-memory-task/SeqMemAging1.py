#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 16, 2020, at 15:24
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'SeqMemAging1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\preeders\\Desktop\\AllenLabSynology\\seqmem_aging\\Task\\Version1\\SeqMemAging1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome to Our Experiment\n\nPlease read the instructions on the next screen\n\nPress the spacebar to continue',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()

# Initialize components for Routine "Blank500ms"
Blank500msClock = core.Clock()
textBlank500ms = visual.TextStim(win=win, name='textBlank500ms',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StudyInstructions"
StudyInstructionsClock = core.Clock()
textStudyInstruct = visual.TextStim(win=win, name='textStudyInstruct',
    text='Study the sequences.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StudyTrial"
StudyTrialClock = core.Clock()
imageStudy = visual.ImageStim(
    win=win,
    name='imageStudy', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Blank500ms"
Blank500msClock = core.Clock()
textBlank500ms = visual.TextStim(win=win, name='textBlank500ms',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "WaitScreen"
WaitScreenClock = core.Clock()
textWait = visual.TextStim(win=win, name='textWait',
    text='The study phase just finished. \nYou will now be tested on the sequences. \nWhen you see "GO", Press the left button if the item is in the correct sequence and press the right button if the item is out of sequence. \nPress the space bar to start',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWait = keyboard.Keyboard()

# Initialize components for Routine "Blank500ms"
Blank500msClock = core.Clock()
textBlank500ms = visual.TextStim(win=win, name='textBlank500ms',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TestTrial"
TestTrialClock = core.Clock()
imageTest = visual.ImageStim(
    win=win,
    name='imageTest', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Jitter"
JitterClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='*',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TestResponse"
TestResponseClock = core.Clock()
keyTestResponse = keyboard.Keyboard()
GOsignal = visual.TextStim(win=win, name='GOsignal',
    text='GO',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500ms"
Blank500msClock = core.Clock()
textBlank500ms = visual.TextStim(win=win, name='textBlank500ms',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
textEnd = visual.TextStim(win=win, name='textEnd',
    text='Thanks for participating.\nPlease see the researcher.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
# keep track of which components have finished
WelcomeScreenComponents = [textWelcome, keyWelcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWelcome.keys = theseKeys.name  # just the last key pressed
            keyWelcome.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500ms"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500msComponents = [textBlank500ms]
for thisComponent in Blank500msComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank500ms"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500msClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500msClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank500ms* updates
    if textBlank500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500ms.frameNStart = frameN  # exact frame index
        textBlank500ms.tStart = t  # local t and not account for scr refresh
        textBlank500ms.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500ms, 'tStartRefresh')  # time at next scr refresh
        textBlank500ms.setAutoDraw(True)
    if textBlank500ms.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500ms.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500ms.tStop = t  # not accounting for scr refresh
            textBlank500ms.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500ms, 'tStopRefresh')  # time at next scr refresh
            textBlank500ms.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500msComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500ms"-------
for thisComponent in Blank500msComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBlank500ms.started', textBlank500ms.tStartRefresh)
thisExp.addData('textBlank500ms.stopped', textBlank500ms.tStopRefresh)

# ------Prepare to start Routine "StudyInstructions"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
StudyInstructionsComponents = [textStudyInstruct]
for thisComponent in StudyInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StudyInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "StudyInstructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StudyInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StudyInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textStudyInstruct* updates
    if textStudyInstruct.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textStudyInstruct.frameNStart = frameN  # exact frame index
        textStudyInstruct.tStart = t  # local t and not account for scr refresh
        textStudyInstruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textStudyInstruct, 'tStartRefresh')  # time at next scr refresh
        textStudyInstruct.setAutoDraw(True)
    if textStudyInstruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textStudyInstruct.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            textStudyInstruct.tStop = t  # not accounting for scr refresh
            textStudyInstruct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textStudyInstruct, 'tStopRefresh')  # time at next scr refresh
            textStudyInstruct.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StudyInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StudyInstructions"-------
for thisComponent in StudyInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textStudyInstruct.started', textStudyInstruct.tStartRefresh)
thisExp.addData('textStudyInstruct.stopped', textStudyInstruct.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialsStudy = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('studytrials\\studytrials2.xlsx', selection='0:6'),
    seed=None, name='trialsStudy')
thisExp.addLoop(trialsStudy)  # add the loop to the experiment
thisTrialsStudy = trialsStudy.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
if thisTrialsStudy != None:
    for paramName in thisTrialsStudy:
        exec('{} = thisTrialsStudy[paramName]'.format(paramName))

for thisTrialsStudy in trialsStudy:
    currentLoop = trialsStudy
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
    if thisTrialsStudy != None:
        for paramName in thisTrialsStudy:
            exec('{} = thisTrialsStudy[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "StudyTrial"-------
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    imageStudy.setImage(ImageFile)
    # keep track of which components have finished
    StudyTrialComponents = [imageStudy]
    for thisComponent in StudyTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StudyTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "StudyTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = StudyTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StudyTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageStudy* updates
        if imageStudy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageStudy.frameNStart = frameN  # exact frame index
            imageStudy.tStart = t  # local t and not account for scr refresh
            imageStudy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageStudy, 'tStartRefresh')  # time at next scr refresh
            imageStudy.setAutoDraw(True)
        if imageStudy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageStudy.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                imageStudy.tStop = t  # not accounting for scr refresh
                imageStudy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageStudy, 'tStopRefresh')  # time at next scr refresh
                imageStudy.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StudyTrial"-------
    for thisComponent in StudyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsStudy.addData('imageStudy.started', imageStudy.tStartRefresh)
    trialsStudy.addData('imageStudy.stopped', imageStudy.tStopRefresh)
    
    # ------Prepare to start Routine "Blank500ms"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500msComponents = [textBlank500ms]
    for thisComponent in Blank500msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank500ms"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500msClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500msClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank500ms* updates
        if textBlank500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank500ms.frameNStart = frameN  # exact frame index
            textBlank500ms.tStart = t  # local t and not account for scr refresh
            textBlank500ms.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank500ms, 'tStartRefresh')  # time at next scr refresh
            textBlank500ms.setAutoDraw(True)
        if textBlank500ms.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank500ms.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank500ms.tStop = t  # not accounting for scr refresh
                textBlank500ms.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank500ms, 'tStopRefresh')  # time at next scr refresh
                textBlank500ms.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500ms"-------
    for thisComponent in Blank500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsStudy.addData('textBlank500ms.started', textBlank500ms.tStartRefresh)
    trialsStudy.addData('textBlank500ms.stopped', textBlank500ms.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsStudy'


# ------Prepare to start Routine "WaitScreen"-------
# update component parameters for each repeat
keyWait.keys = []
keyWait.rt = []
# keep track of which components have finished
WaitScreenComponents = [textWait, keyWait]
for thisComponent in WaitScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WaitScreen"-------
while continueRoutine:
    # get current time
    t = WaitScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWait* updates
    if textWait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWait.frameNStart = frameN  # exact frame index
        textWait.tStart = t  # local t and not account for scr refresh
        textWait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWait, 'tStartRefresh')  # time at next scr refresh
        textWait.setAutoDraw(True)
    
    # *keyWait* updates
    waitOnFlip = False
    if keyWait.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        keyWait.frameNStart = frameN  # exact frame index
        keyWait.tStart = t  # local t and not account for scr refresh
        keyWait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWait, 'tStartRefresh')  # time at next scr refresh
        keyWait.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWait.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWait.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWait.status == STARTED and not waitOnFlip:
        theseKeys = keyWait.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWait.keys = theseKeys.name  # just the last key pressed
            keyWait.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitScreen"-------
for thisComponent in WaitScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWait.started', textWait.tStartRefresh)
thisExp.addData('textWait.stopped', textWait.tStopRefresh)
# check responses
if keyWait.keys in ['', [], None]:  # No response was made
    keyWait.keys = None
thisExp.addData('keyWait.keys',keyWait.keys)
if keyWait.keys != None:  # we had a response
    thisExp.addData('keyWait.rt', keyWait.rt)
thisExp.addData('keyWait.started', keyWait.tStartRefresh)
thisExp.addData('keyWait.stopped', keyWait.tStopRefresh)
thisExp.nextEntry()
# the Routine "WaitScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500ms"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500msComponents = [textBlank500ms]
for thisComponent in Blank500msComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank500ms"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500msClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500msClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank500ms* updates
    if textBlank500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500ms.frameNStart = frameN  # exact frame index
        textBlank500ms.tStart = t  # local t and not account for scr refresh
        textBlank500ms.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500ms, 'tStartRefresh')  # time at next scr refresh
        textBlank500ms.setAutoDraw(True)
    if textBlank500ms.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500ms.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500ms.tStop = t  # not accounting for scr refresh
            textBlank500ms.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500ms, 'tStopRefresh')  # time at next scr refresh
            textBlank500ms.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500msComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500ms"-------
for thisComponent in Blank500msComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBlank500ms.started', textBlank500ms.tStartRefresh)
thisExp.addData('textBlank500ms.stopped', textBlank500ms.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialsTest = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('studytrials\\studytrials2.xlsx', selection='6:13'),
    seed=None, name='trialsTest')
thisExp.addLoop(trialsTest)  # add the loop to the experiment
thisTrialsTest = trialsTest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsTest.rgb)
if thisTrialsTest != None:
    for paramName in thisTrialsTest:
        exec('{} = thisTrialsTest[paramName]'.format(paramName))

for thisTrialsTest in trialsTest:
    currentLoop = trialsTest
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest.rgb)
    if thisTrialsTest != None:
        for paramName in thisTrialsTest:
            exec('{} = thisTrialsTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TestTrial"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    imageTest.setImage(ImageFile)
    # keep track of which components have finished
    TestTrialComponents = [imageTest]
    for thisComponent in TestTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "TestTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TestTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTest* updates
        if imageTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTest.frameNStart = frameN  # exact frame index
            imageTest.tStart = t  # local t and not account for scr refresh
            imageTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTest, 'tStartRefresh')  # time at next scr refresh
            imageTest.setAutoDraw(True)
        if imageTest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTest.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                imageTest.tStop = t  # not accounting for scr refresh
                imageTest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTest, 'tStopRefresh')  # time at next scr refresh
                imageTest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestTrial"-------
    for thisComponent in TestTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsTest.addData('imageTest.started', imageTest.tStartRefresh)
    trialsTest.addData('imageTest.stopped', imageTest.tStopRefresh)
    
    # ------Prepare to start Routine "Jitter"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    JitterComponents = [Fixation]
    for thisComponent in JitterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    JitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Jitter"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = JitterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=JitterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in JitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Jitter"-------
    for thisComponent in JitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsTest.addData('Fixation.started', Fixation.tStartRefresh)
    trialsTest.addData('Fixation.stopped', Fixation.tStopRefresh)
    
    # ------Prepare to start Routine "TestResponse"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    keyTestResponse.keys = []
    keyTestResponse.rt = []
    # keep track of which components have finished
    TestResponseComponents = [keyTestResponse, GOsignal]
    for thisComponent in TestResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "TestResponse"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TestResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyTestResponse* updates
        waitOnFlip = False
        if keyTestResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyTestResponse.frameNStart = frameN  # exact frame index
            keyTestResponse.tStart = t  # local t and not account for scr refresh
            keyTestResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyTestResponse, 'tStartRefresh')  # time at next scr refresh
            keyTestResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyTestResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyTestResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyTestResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyTestResponse.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                keyTestResponse.tStop = t  # not accounting for scr refresh
                keyTestResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyTestResponse, 'tStopRefresh')  # time at next scr refresh
                keyTestResponse.status = FINISHED
        if keyTestResponse.status == STARTED and not waitOnFlip:
            theseKeys = keyTestResponse.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                keyTestResponse.keys = theseKeys.name  # just the last key pressed
                keyTestResponse.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *GOsignal* updates
        if GOsignal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GOsignal.frameNStart = frameN  # exact frame index
            GOsignal.tStart = t  # local t and not account for scr refresh
            GOsignal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GOsignal, 'tStartRefresh')  # time at next scr refresh
            GOsignal.setAutoDraw(True)
        if GOsignal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GOsignal.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                GOsignal.tStop = t  # not accounting for scr refresh
                GOsignal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(GOsignal, 'tStopRefresh')  # time at next scr refresh
                GOsignal.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestResponse"-------
    for thisComponent in TestResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyTestResponse.keys in ['', [], None]:  # No response was made
        keyTestResponse.keys = None
    trialsTest.addData('keyTestResponse.keys',keyTestResponse.keys)
    if keyTestResponse.keys != None:  # we had a response
        trialsTest.addData('keyTestResponse.rt', keyTestResponse.rt)
    trialsTest.addData('keyTestResponse.started', keyTestResponse.tStartRefresh)
    trialsTest.addData('keyTestResponse.stopped', keyTestResponse.tStopRefresh)
    trialsTest.addData('GOsignal.started', GOsignal.tStartRefresh)
    trialsTest.addData('GOsignal.stopped', GOsignal.tStopRefresh)
    
    # ------Prepare to start Routine "Blank500ms"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500msComponents = [textBlank500ms]
    for thisComponent in Blank500msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank500ms"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500msClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500msClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank500ms* updates
        if textBlank500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank500ms.frameNStart = frameN  # exact frame index
            textBlank500ms.tStart = t  # local t and not account for scr refresh
            textBlank500ms.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank500ms, 'tStartRefresh')  # time at next scr refresh
            textBlank500ms.setAutoDraw(True)
        if textBlank500ms.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank500ms.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank500ms.tStop = t  # not accounting for scr refresh
                textBlank500ms.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank500ms, 'tStopRefresh')  # time at next scr refresh
                textBlank500ms.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500ms"-------
    for thisComponent in Blank500msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsTest.addData('textBlank500ms.started', textBlank500ms.tStartRefresh)
    trialsTest.addData('textBlank500ms.stopped', textBlank500ms.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsTest'


# ------Prepare to start Routine "EndScreen"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
EndScreenComponents = [textEnd, key_resp]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "EndScreen"-------
while continueRoutine:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEnd* updates
    if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEnd.frameNStart = frameN  # exact frame index
        textEnd.tStart = t  # local t and not account for scr refresh
        textEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
        textEnd.setAutoDraw(True)
    if textEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEnd.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            textEnd.tStop = t  # not accounting for scr refresh
            textEnd.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEnd, 'tStopRefresh')  # time at next scr refresh
            textEnd.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['i', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEnd.started', textEnd.tStartRefresh)
thisExp.addData('textEnd.stopped', textEnd.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
