from progress_bar import DotCircledProgressBar
import pygame
import pygwidgets
import time
import random
from matrix import MatrixUi

def draw_all():
    """
    draw all the buttons, text fields and else things.
    """
    global line1, line2, line3, line4_1, line4_2, line4_2
    global answertext, mode_text, backspace, text
    text.draw()
    answertext.draw()
    mode_text.draw()
    line1.drawAllButtons()
    line2.drawAllButtons()
    line3.drawAllButtons()
    line4_1.drawAllButtons()
    line4_2.drawAllButtons()
    line5.drawAllButtons()
    backspace.draw()

# 加载动画
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((1004, 610))
window.fill((0, 191, 255))
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption('Collections of calculation')
pygame.display.update()
loading_obj = DotCircledProgressBar(window, clock, (502, 300), 100, 10, (0, 191, 255))
loading_obj.run()
loading = pygwidgets.DisplayText(window, (100, 450), 'Including packages...7% complete',
                                 textColor=(255, 255, 255), backgroundColor=(0, 191, 255), fontSize=40,
                                 fontName='fonts/JetBrainsMono-Light.ttf')
loading.draw()
import math
import sys
import pyghelpers

loading.setValue('Including packages...15% complete')
loading.draw()
# 19%
import numpy as np

loading.setValue('Including packages...31% complete')
loading.draw()
# 39%
import sympy

loading.setValue('Including packages...57% complete')
loading.draw()

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('WXagg')
ax = plt.gca()

loading.setValue('Including packages...81% complete')
loading.draw()
# 79%
from buttoncenter import *
from mathwork import mathwork

loading.setValue('Including packages...94% complete')
loading.draw()

from statistics import data_visualize, Message_window, data_analyze, data_comparison, data_distribution
from checkbox import CheckBox
from progress_bar import windows_progress_bar
import pyperclip

loading.setValue('Including packages...100% complete')
loading.draw()
time.sleep(0.2)
pygame.font.init()
loading_obj.done()
"""
----------------------------
| version: 7.0             |
| develop time: 2025-1-19  |
----------------------------
"""

############################################################
#init all the things----------------------------------------
############################################################
message_window = Message_window()
xticks_angle = -45
mode = 'DEG'
functions = ["sin", "cos", "tan", 'arcsin', "arccos", "arctan", "log", "ln", "root", 'min']
plt.rcParams['font.family'] = 'SimHei'; plt.rcParams['axes.unicode_minus'] = False
ax.spines['top'].set_color('none'); ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0.5)); ax.spines['bottom'].set_position(('data', 0))
plt.grid(True, linestyle="--", alpha=0.5)
"""linestyle:
'-' 	solid line style
'--' 	dashed line style
'-.' 	dash-dot line style
':' 	dotted line style
'.' 	point marker
',' 	pixel marker
'o' 	circle marker
'v' 	triangle_down marker
'^' 	triangle_up marker
'<' 	triangle_left marker
'>' 	triangle_right marker
'1' 	tri_down marker
'2' 	tri_up marker
'3' 	tri_left marker
'4' 	tri_right marker
's' 	square marker
'p' 	pentagon marker
'*' 	star marker
'h' 	hexagon1 marker
'H' 	hexagon2 marker
'+' 	plus marker
'x' 	x marker
'D' 	diamond marker
'd' 	thin_diamond marker
'|' 	vline marker
'_' 	hline marker"""

x = sympy.symbols('x')
y = sympy.symbols('y')
z = sympy.symbols('z')
mathtext = ''
font_path = 'fonts/JetBrainsMono-Light.ttf'
line1 = ButtonCenter(None, (0, 0, 0), (90, 90, 150), (0, 50, 100), (20, 0, 80), 16,
                     ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', 'C'],
                     window, 60, 60, 0, 92, 62, 0, font=font_path, font_size=18, callbacks=None)

line2 = ButtonCenter(None, (0, 0, 0), (90, 90, 150), (0, 50, 100), (20, 0, 80), 16,
                     ['(', ')', 'M', 'M+', 'Rad', 'Deg', 'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', '!',
                      'alog(x)', 'ln(x)', '(a)√(x)'], window, 60, 60, 0, 152, 62, 0, font=font_path, font_size=11,
                     callbacks=None)

line3 = ButtonCenter(None, (0, 0, 0), (90, 90, 150), (0, 50, 100), (20, 0, 80), 7,
                     ['.', 'e', 'π', '^', 'integral', 'double integral', 'triple integral']
                     , window, 120, 60, 0, 212, 124, 0, font=font_path, font_size=11, callbacks=None)

line4_1 = ButtonCenter(None, (0, 0, 0), (90, 90, 150), (0, 50, 100), (20, 0, 80), 3,
                       ['differential(s)', 'function image', 'data visualize'], window, 160, 60, 0, 272, 160,
                       0, font=font_path, font_size=14, callbacks=None)

line4_2 = ButtonCenter(None, (0, 0, 0), (90, 90, 150), (0, 50, 100), (20, 0, 80), 4,
                       ['(-)', 'percent', 'simplify', 'solve'], window, 120, 60, 482, 272, 124, 0
                       , font=font_path, font_size=14, callbacks=None)

line5 = ButtonCenter(None, (0, 0, 0), (90, 90, 150), (0, 50, 100), (20, 0, 80), 7,
                     ['limit', 'clean memory', 'copy answer', 'data analyze', 'distribution', 'comparison', 'matrix'], window, 120, 60, 0, 332, 124, 0, font=font_path,
                     font_size=14, callbacks=None)

answer = ''
backspace = pygwidgets.TextButton(window, (870, 212), 'backspace', 120, 60, textColor=(0, 0, 0), upColor=(90, 90, 150),
                                  overColor=(0, 50, 100), downColor=(20, 0, 80), fontName=font_path, fontSize=18)
usr_showing_maths_texts = ''
text = pygwidgets.DisplayText(window, (0, 0), usr_showing_maths_texts, font_path, 60, 1004, backgroundColor=(255, 255, 255), height=90)
answertext = pygwidgets.DisplayText(window, (0, 570), '', font_path, 30, 1004, backgroundColor=(255, 255, 255),
                                    height=40)
left = 0
right = 0
MEMORY = ('', '')
point = True
matrix_saved_data = ({}, [], None)
func = 0
mode_text = pygwidgets.DisplayText(window, (910, 65), 'mode:' + mode, textColor=(100, 100, 100),
                                   backgroundColor=(255, 255, 255), fontName=font_path)
draw_all()
pygame.display.update()
###############################################################################################################
#main loop-----------------------------------------------------------------------------------------------------
###############################################################################################################
while True:
    mode_text.setValue('mode:'+mode)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        window.fill((0, 191, 255))
        if len(usr_showing_maths_texts) <= 32:
            text = pygwidgets.DisplayText(window, (0, 0), usr_showing_maths_texts, font_path, 50, 1004, backgroundColor=(255, 255, 255),
                                          height=90)
        elif len(usr_showing_maths_texts) <= 42:
            text = pygwidgets.DisplayText(window, (0, 0), usr_showing_maths_texts, font_path, 40, 1004, backgroundColor=(255, 255, 255),
                                          height=90)
        elif len(usr_showing_maths_texts) <= 55:
            text = pygwidgets.DisplayText(window, (0, 0), usr_showing_maths_texts, font_path, 30, 1004, backgroundColor=(255, 255, 255),
                                          height=90)
        elif len(usr_showing_maths_texts) <= 110:
            # 双行显示
            text.setValue(usr_showing_maths_texts[0:56])
            text2 = pygwidgets.DisplayText(window, (0, 30), usr_showing_maths_texts[55:111], font_path, 30, 1004,
                                           backgroundColor=(255, 255, 255),
                                           height=60)
            text2.draw()
        else:
            over = len(usr_showing_maths_texts) - 165
            if len(usr_showing_maths_texts) >= 165:
                message_window.warning(
                    "The length of the string that you input is longer than the max number(165):" + str(len(usr_showing_maths_texts)) +
                    ', suggesting canceling the formula into a shorter one, or the screen won' + "'"
                    + 't be able to show all characters.')
            if over <= 0:
                text.setValue(usr_showing_maths_texts[0:56])
                text2 = pygwidgets.DisplayText(window, (0, 30), usr_showing_maths_texts[55:111], font_path, 30, 1004,
                                               backgroundColor=(255, 255, 255),
                                               height=30)
                text3 = pygwidgets.DisplayText(window, (0, 60), usr_showing_maths_texts[110:166], font_path, 30, 1004,
                                               backgroundColor=(255, 255, 255),
                                               height=30)
            else:
                text.setValue(usr_showing_maths_texts[0:56])
                text2 = pygwidgets.DisplayText(window, (0, 30), usr_showing_maths_texts[55 + over:111 + over], font_path, 30, 1004,
                                               backgroundColor=(255, 255, 255),
                                               height=30)
                text3 = pygwidgets.DisplayText(window, (0, 60), usr_showing_maths_texts[110 + over:166 + over], font_path, 30, 1004,
                                               backgroundColor=(255, 255, 255),
                                               height=30)
            text2.draw()
            text3.draw()
        draw_all()
        event_proceeded = False

        for i in line1.Buttons:
            INDEX = line1.Buttons.index(i)
            if i.handleEvent(event):
                if INDEX < 10:  # 输入数字
                    usr_showing_maths_texts += str(INDEX)
                    mathtext += str(INDEX)
                else:
                    if INDEX == 15:
                        usr_showing_maths_texts = ''
                        mathtext = ''
                        answer = ''
                        point = True
                    elif INDEX == 10:
                        usr_showing_maths_texts += '+'
                        point = True
                        if left > right:  # 当前输入的是函数的参数
                            mathtext += '+'
                        else:
                            mathtext += ' + '  # 在[]外
                            func = 0
                    elif INDEX == 11:
                        usr_showing_maths_texts += '-'
                        point = True
                        if left > right:  # 当前输入的是函数的参数
                            mathtext += '-'
                        else:
                            mathtext += ' - '  # 在[]外
                            func = 0
                    elif INDEX == 12:
                        usr_showing_maths_texts += '*'
                        point = True
                        if left > right:  # 当前输入的是函数的参数
                            mathtext += '*'
                        else:
                            mathtext += ' * '  # 在[]外
                            func = 0
                    elif INDEX == 13:
                        usr_showing_maths_texts += '/'
                        point = True
                        if left > right:  # 当前输入的是函数的参数
                            mathtext += '/'
                        else:
                            mathtext += ' / '  # 在[]外
                            func = 0
                    elif INDEX == 14:
                        try:
                            if mode == 'RAD':
                                print(mathtext)
                                text_ = mathwork(mathtext, 'RAD')
                                if 'ERROR' in str(text_):
                                    message_window.error(str(text_))
                                else:
                                    answertext.setValue(text_)
                                    answer = str(text_)
                            else:
                                text_ = mathwork(mathtext, 'DEG')
                                #print(text_)
                                if 'ERROR' in str(text_):
                                    message_window.error(str(text_))
                                else:
                                    answertext.setValue(text_)
                                    answer = str(text_)

                        except Exception as e:
                            message_window.error(str(e) + ',please recheck your input')
                    # print(mathtext)
                event_proceeded = True
                break

        if event_proceeded:
            continue
        event_proceeded = False

        for i in line2.Buttons:
            INDEX = line2.Buttons.index(i)
            if i.handleEvent(event):
                if INDEX == 0:
                    usr_showing_maths_texts += '('
                    if not func:
                        if left > right:  # 当前输入的是函数的参数
                            mathtext += '('
                        else:
                            mathtext += ' ( '
                    else:
                        mathtext += '['
                        left += 1
                elif INDEX == 1:
                    usr_showing_maths_texts += ')'
                    if not func:
                        if left > right:  # 当前输入的是函数的参数

                            mathtext += ')'
                        else:
                            mathtext += ' ) '
                    else:
                        mathtext += ']'
                        right += 1
                        if left == right:  # means exit from present function
                            left = 0
                            right = 0
                            func = 0
                elif INDEX == 2:  # unused button
                    MEMORY = (usr_showing_maths_texts, mathtext)
                elif INDEX == 3:  # unused button
                    usr_showing_maths_texts, mathtext = MEMORY
                elif INDEX == 4:
                    mode = 'RAD'
                elif INDEX == 5:
                    mode = 'DEG'
                elif INDEX == 6:
                    usr_showing_maths_texts += 'sin'
                    mathtext += 'sin;'
                    func = 1
                elif INDEX == 7:
                    usr_showing_maths_texts += 'cos'
                    mathtext += 'cos;'
                    func = 1
                elif INDEX == 8:
                    usr_showing_maths_texts += 'tan'
                    mathtext += 'tan;'
                    func = 1
                elif INDEX == 9:
                    usr_showing_maths_texts += 'arcsin'
                    mathtext += 'arcsin;'
                    func = 1
                elif INDEX == 10:
                    usr_showing_maths_texts += 'arccos'
                    mathtext += 'arccos;'
                    func = 1
                elif INDEX == 11:
                    usr_showing_maths_texts += 'arctan'
                    mathtext += 'arctan;'
                    func = 1
                elif INDEX == 12:
                    usr_showing_maths_texts += '!'
                    mathtext += '!'
                    func = 1
                elif INDEX == 13:
                    usr_showing_maths_texts += 'log'
                    mathtext += 'log'
                    func = 1
                elif INDEX == 14:
                    usr_showing_maths_texts += 'ln'
                    mathtext += 'ln'
                    func = 1
                elif INDEX == 15:
                    usr_showing_maths_texts += '√'
                    mathtext += 'root'
                    func = 1
                event_proceeded = True
                break

        if event_proceeded:
            continue
        event_proceeded = False

        for i in line3.Buttons:
            INDEX = line3.Buttons.index(i)
            if i.handleEvent(event):
                if INDEX == 0:
                    if point:
                        usr_showing_maths_texts += '.'
                        mathtext += '.'
                        point = False
                    else:
                        i.disable()
                elif INDEX == 1:
                    point = False
                    usr_showing_maths_texts += 'e'
                    mathtext += str(math.e)
                elif INDEX == 2:
                    point = False
                    usr_showing_maths_texts += 'π'
                    mathtext += str(math.pi)
                elif INDEX == 3:
                    point = True
                    usr_showing_maths_texts += '^'
                    mathtext += '^'
                elif INDEX == 4:
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input you formula here( y/z = f(x /x,y)=', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in formula:
                            pass
                    except TypeError:
                        continue
                    if not ('x' in formula or 'y' in formula):
                        answertext.setValue('you are not input a formula')
                        answer = ''
                    else:
                        answertext.setValue('')
                        choise = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300), 'TYPE', 'definite integral',
                                                            'indefinite integral')  # None表示只有一个选项
                        x = sympy.symbols('x')
                        y = sympy.symbols('y')
                        z = sympy.symbols('z')

                        if choise:  # 不定积分
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                                 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            if not choise2:  # 对y积分
                                Answer = sympy.integrate(sympy.sympify(formula), y)
                                answertext.setValue(Answer)
                                answer = str(Answer)
                            else:  # 对x积分
                                Answer = sympy.integrate(sympy.sympify(formula), x)
                                answertext.setValue(Answer)
                                answer = str(Answer)
                        else:
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                                 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            if not choise2:  # 对y积分
                                out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input maximum', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out1:
                                    continue
                                out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input minimum', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out2:
                                    continue
                                Answer = sympy.integrate(sympy.sympify(formula), (y, float(out2), float(out1)))
                                answertext.setValue(Answer)
                                answer = str(Answer)
                            else:  # 对x积分
                                out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input maximum', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out1:
                                    continue
                                out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input minimum', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out2:
                                    continue
                                Answer = sympy.integrate(sympy.sympify(formula), (x, float(out2), float(out1)))
                                answertext.setValue(Answer)
                                answer = str(Answer)
                elif INDEX == 5:
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input you formula here( y/z = f(x /x,y)=', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in formula:
                            pass
                    except TypeError:
                        continue

                    answertext.setValue('')
                    mathtext = ''
                    usr_showing_maths_texts = ''
                    choise = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300), 'TYPE', 'definite integral',
                                                        'indefinite integral')  # None表示只有一个选项
                    x = sympy.symbols('x')
                    y = sympy.symbols('y')
                    z = sympy.symbols('z')

                    if choise:  # 不定积分

                        choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                             'to', 'x  (dx)',
                                                             'y  (dy)')  # None表示只有一个选项
                        if not choise2:  # 对y积分
                            Answer = sympy.integrate(sympy.sympify(formula), y)
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                                 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            if not choise2:  # 对y积分
                                Answer = sympy.integrate(sympy.sympify(Answer), y)

                            else:  # 对x积分
                                Answer = sympy.integrate(sympy.sympify(Answer), x)
                            answertext.setValue(Answer)
                            answer = str(Answer)
                        else:  # 对x积分
                            Answer = sympy.integrate(sympy.sympify(formula), x)
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                                 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            if not choise2:  # 对y积分
                                Answer = sympy.integrate(sympy.sympify(Answer), y)

                            else:  # 对x积分
                                Answer = sympy.integrate(sympy.sympify(Answer), x)
                            answertext.setValue(Answer)
                            answer = str(Answer)
                    else:
                        choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                             'to', 'x  (dx)',
                                                             'y  (dy)')  # None表示只有一个选项
                        if not choise2:  # 对y积分
                            out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                               'input maximum(out)', 'OK',
                                                               'cancel', backgroundColor=(90, 90, 150),
                                                               promptTextColor=(0, 0, 0),
                                                               inputTextColor=(0, 0, 0))
                            if not out1:
                                continue
                            out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                               'input minimum(out)', 'OK',
                                                               'cancel', backgroundColor=(90, 90, 150),
                                                               promptTextColor=(0, 0, 0),
                                                               inputTextColor=(0, 0, 0))
                            if not out2:
                                continue
                            Answer = sympy.integrate(sympy.sympify(formula), (y, out2, out1))
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                                 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            if not choise2:  # 对y积分
                                out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input maximum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out1:
                                    continue
                                out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input minimum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out2:
                                    continue
                                Answer = sympy.integrate(sympy.sympify(formula), (y, out2, out1))
                                answertext.setValue(Answer)
                                answer = str(Answer)
                            else:  # 对x积分
                                out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input maximum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out1:
                                    continue
                                out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input minimum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out2:
                                    continue
                                Answer = sympy.integrate(sympy.sympify(formula), (x, out2, out1))
                                answertext.setValue(Answer)
                                answer = str(Answer)
                        else:  # 对x积分
                            out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                               'input maximum(out)', 'OK',
                                                               'cancel', backgroundColor=(90, 90, 150),
                                                               promptTextColor=(0, 0, 0),
                                                               inputTextColor=(0, 0, 0))
                            if not out1:
                                continue
                            out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                               'input minimum(out)', 'OK',
                                                               'cancel', backgroundColor=(90, 90, 150),
                                                               promptTextColor=(0, 0, 0),
                                                               inputTextColor=(0, 0, 0))
                            if not out2:
                                continue
                            Answer = sympy.integrate(sympy.sympify(formula), (x, out2, out1))
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300),
                                                                 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            if not choise2:  # 对y积分
                                out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input maximum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out1:
                                    continue
                                out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input minimum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out2:
                                    continue
                                Answer = sympy.integrate(sympy.sympify(formula), (y, out2, out1))
                                answertext.setValue(Answer)
                                answer = str(Answer)
                            else:  # 对x积分
                                out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input maximum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out1:
                                    continue
                                out2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                   'input minimum(mid)', 'OK',
                                                                   'cancel', backgroundColor=(90, 90, 150),
                                                                   promptTextColor=(0, 0, 0),
                                                                   inputTextColor=(0, 0, 0))
                                if not out2:
                                    continue
                                Answer = sympy.integrate(sympy.sympify(Answer), (x, out2, out1))
                                answertext.setValue(Answer)
                                answer = str(Answer)
                elif INDEX == 6:
                    list = []
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input you formula here( y/z = f(x /x,y)=', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in formula:
                            pass
                    except TypeError:
                        continue

                    answertext.setValue('')
                    choise = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300), 'TYPE', 'definite integral',
                                                        'indefinite integral')  # None表示只有一个选项
                    x = sympy.symbols('x')
                    y = sympy.symbols('y')
                    z = sympy.symbols('z')
                    if not choise:
                        for i2 in range(3):
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300), 'to', 'x  (dx)',
                                                                 'y  (dy)')  # None表示只有一个选项
                            list.append(choise2)
                        if list[0]:  # 对x积分
                            Answer = sympy.integrate(sympy.sympify(formula), x)
                        else:
                            Answer = sympy.integrate(sympy.sympify(formula), x)
                        for i in range(2):
                            if list[i + 1]:
                                Answer = sympy.integrate(sympy.sympify(Answer), x)
                            else:
                                Answer = sympy.integrate(sympy.sympify(Answer), y)
                        answertext.setValue(Answer)
                        answer = str(Answer)
                    else:
                        agrements = []
                        for i2 in range(3):
                            choise2 = pyghelpers.textYesNoDialog(window, (0, 300, 400, 300), 'to', 'x  (dx)'
                                                                 , 'y  (dy)')  # None表示只有一个选项
                            list.append(choise2)
                            out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                               'input maximum(from outside to inside)', 'OK',
                                                               'cancel', backgroundColor=(90, 90, 150),
                                                               promptTextColor=(0, 0, 0),
                                                               inputTextColor=(0, 0, 0))
                            if not out1:
                                continue
                            agrements.append(out1)
                            out1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                               'input minimum(from outside to inside)', 'OK',
                                                               'cancel', backgroundColor=(90, 90, 150),
                                                               promptTextColor=(0, 0, 0),
                                                               inputTextColor=(0, 0, 0))
                            if not out1:
                                continue
                            agrements.append(out1)
                        Answer = sympy.integrate(sympy.sympify(formula), (x, agrements[1], agrements[0]))
                        if len(agrements) == 6:
                            for i2 in range(2):
                                Answer = sympy.integrate(sympy.sympify(Answer),
                                                         (x, agrements[i2 + 3], agrements[i2 + 2]))
                        else:
                            Answer = 'ERROR'
                        answertext.setValue(Answer)
                        answer = str(Answer)
                event_proceeded = True
                break

        if event_proceeded:
            continue
        event_proceeded = False

        for i in line4_1.Buttons:
            INDEX = line4_1.Buttons.index(i)
            if i.handleEvent(event):
                if INDEX == 0:
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input you formula here( y/z = f(x[,y])=', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in formula:
                            pass
                    except TypeError:
                        continue
                    answertext.setValue('')
                    num = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                      'how many times do you want to differential at all', 'OK',
                                                      'CANCEL', backgroundColor=(90, 90, 150),
                                                      promptTextColor=(0, 0, 0),
                                                      inputTextColor=(0, 0, 0))
                    try:
                        if num == 0:
                            continue
                        c = int(num)
                    except Exception:
                        continue
                    break_ = False
                    Answer = None
                    for c2 in range(int(num) - 1):
                        check = CheckBox(3, ['to x', 'to y', 'to z'], 1, window, clock, 300, 300, each_add_x=0,
                                         each_add_y=10)
                        if len(check.clicked_choices) == 1:
                            check = str(check.clicked_choices[0])
                        else:
                            message_window.error('exit because of no choice selected')
                            break_ = True
                            break
                        x = sympy.symbols('x')
                        y = sympy.symbols('y')
                        z = sympy.symbols('z')
                        formula = sympy.sympify(formula)
                        if c2 == 0:
                            if check == '1':
                                Answer = formula.diff(x, 1)
                            elif check == '2':
                                Answer = formula.diff(y, 1)
                            elif check == '3':
                                Answer = formula.diff(z, 1)
                            else:
                                answertext.setValue('')
                                break
                        else:
                            if check == '1':
                                Answer = Answer.diff(x, 1)
                            elif check == '2':
                                Answer = Answer.diff(y, 1)
                            elif check == '3':
                                Answer = Answer.diff(z, 1)
                            else:
                                answertext.setValue('')
                                break
                    if not break_:
                        answertext.setValue(Answer)
                        answer = str(Answer)
                elif INDEX == 1:

                    ploter = True
                    choise3 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'how many line(s) do you want to draw?', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    try:
                        c = int(choise3)
                    except TypeError or ValueError:
                        message_window.warning('WARNING!you are not input a integer')
                        continue
                    if int(choise3) < 1:
                        continue
                    x1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                     'max x', 'OK',
                                                     'CANCEL', backgroundColor=(90, 90, 150),
                                                     promptTextColor=(0, 0, 0),
                                                     inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in x1:
                            pass
                    except TypeError:
                        continue
                    x2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                     'min x', 'OK', 'CANCEL', backgroundColor=(90, 90, 150),
                                                     promptTextColor=(0, 0, 0),
                                                     inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in x2:
                            pass
                    except TypeError:
                        continue
                    y1 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                     'max y', 'OK',
                                                     'CANCEL', backgroundColor=(90, 90, 150),
                                                     promptTextColor=(0, 0, 0),
                                                     inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in y1:
                            pass
                    except TypeError:
                        continue
                    y2 = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                     'min y', 'OK',
                                                     'CANCEL', backgroundColor=(90, 90, 150),
                                                     promptTextColor=(0, 0, 0),
                                                     inputTextColor=(0, 0, 0))
                    try:
                        if 'x' in y2:
                            pass
                    except TypeError:
                        continue

                    _x = np.linspace(float(x2), float(x1), 1000)
                    _xs = []
                    bar = windows_progress_bar(1000 * (int(choise3)), window, title='charting...')
                    bar.show()
                    for c in range(int(choise3)):  # start drawing
                        bar.pause()
                        formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                              'input you formula to draw here y = f(x) =', 'OK',
                                                              'CANCEL', backgroundColor=(90, 90, 150),
                                                              promptTextColor=(0, 0, 0),
                                                              inputTextColor=(0, 0, 0))
                        try:
                            if 'x' in formula:
                                pass
                        except TypeError:
                            ploter = False
                            break
                        label = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                            'input you lable', 'OK',
                                                            'CANCEL', backgroundColor=(90, 90, 150),
                                                            promptTextColor=(0, 0, 0),
                                                            inputTextColor=(0, 0, 0))
                        try:
                            if 'x' in label:
                                pass
                        except TypeError:
                            label = ''
                        Answer = sympy.sympify('(' + formula + ')-y')  # 对y求值
                        Formula = sympy.lambdify(sympy.symbols('x'), Answer, 'numpy')
                        _ys = []
                        _xs = []
                        bar.continue_draw()
                        for d, e in zip(_x, range(len(_x))):
                            bar.start()
                            _y = sympy.solve(Answer, y)  # 计算出合适的y值并加入列表中
                            x_value = d
                            _xs.append(x_value)
                            if len(_y) < 2:
                                y_val = _y[0].subs(x, d)
                                _ys.append(y_val)
                            else:
                                for i2 in range(len(_y)):
                                    y_val = _y[i2].subs(x, d)
                                    _ys.append(y_val)
                                    if i2 > 0:
                                        x_value = d
                                        _xs.append(x_value)
                            bar.update_time(e + 1 + c * 1000)
                        if label:
                            plt.plot(_xs, _ys, label=label)
                        else:
                            plt.plot(_xs, _ys)
                        plt.axis((x2, x1, y2, y1))  # initialize the board
                        plt.xlim(0, float(x1))
                        plt.ylim(0, float(y1))
                        xticks = np.linspace(float(x1), float(x2), 21)

                        xtick = []
                        for i in xticks:
                            if (abs(i) > 1000 or abs(i) < 0.001) and i != 0:
                                xtick.append('{:.4e}'.format(i))
                            else:
                                xtick.append(str(i)[0:5])
                        plt.xticks(ticks=xticks, labels=xtick, rotation=xticks_angle)
                        yticks = np.linspace(float(y1), float(y2), 21)
                        ytick = []
                        for i in yticks:
                            if abs(i) > 1000 or abs(i) < 0.001 and i != 0:
                                ytick.append('{:.4e}'.format(i))
                            else:
                                ytick.append(str(i)[0:5])
                        plt.yticks(ticks=yticks, labels=ytick)
                    if ploter:
                        plt.legend()  # 显示文本
                        plt.show()
                elif INDEX == 2:  # data visualize
                    data_visualize(window, clock)
                event_proceeded = True
                break

        if event_proceeded:
            continue
        event_proceeded = False

        for i in line4_2.Buttons:
            INDEX = line4_2.Buttons.index(i)
            if i.handleEvent(event):
                if INDEX == 0:
                    usr_showing_maths_texts += '-'
                    mathtext += '-'
                elif INDEX == 1:
                    usr_showing_maths_texts += '%'
                    mathtext += '%'
                elif INDEX == 2:
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input the formula that you want to simplify', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    if formula != None:
                        try:
                            if '=' in formula:
                                message_window.error("Can't simplify a equation!!!")
                            simplified_formula = sympy.sympify(formula)
                            answertext.setValue(str(simplified_formula))
                            answer = str(simplified_formula)
                        except Exception as e:
                            message_window.error(
                                "Can't simplify the formula:" + formula + ", due to the Error:" + str(e))
                    else:
                        message_window.error("Failed to simplify due to an empty formula was given")
                elif INDEX == 3:
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input the formula(s) that you want to solve(equals 0), '
                                                          'split with ";"',
                                                          'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    if formula is not None:
                        all_formulas = formula.split(';')
                        all_formulas = [i for i in all_formulas if i is not None]
                        for current, index in zip(all_formulas, range(len(all_formulas))):
                            if '=' in current:
                                left, right = current.split('=')[0], current.split('=')[1]
                                all_formulas[index] = left + '-(' + right + ')'
                        symbols = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                              'input the symbol(s) that you use in the formula:' + str(
                                                                  formula) + ',split with ";"',
                                                              'OK',
                                                              'CANCEL', backgroundColor=(90, 90, 150),
                                                              promptTextColor=(0, 0, 0),
                                                              inputTextColor=(0, 0, 0))
                        symbols = symbols.split(';')
                        symbols = [i for i in symbols if i is not None]
                        try:
                            symbols_used = [sympy.symbols(i) for i in symbols]
                            simpified_formula = [sympy.sympify(i) for i in all_formulas]
                            answers = sympy.solve(simpified_formula, symbols_used, dict=True)
                            answertext.setValue(str(answers))
                            answer = str(answers)
                        except Exception as e:
                            message_window.error(
                                "Can't solve the formula:" + formula + ", due to the Error:" + str(e))
                    else:
                        message_window.error("Failed to solve the formula due to an empty formula was given")
                event_proceeded = True
                break

        if event_proceeded:
            continue
        event_proceeded = False

        for i in line5.Buttons:
            INDEX = line5.Buttons.index(i)
            if i.handleEvent(event):
                if INDEX == 0:
                    formula = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                          'input the formula that you want to get the limit', 'OK',
                                                          'CANCEL', backgroundColor=(90, 90, 150),
                                                          promptTextColor=(0, 0, 0),
                                                          inputTextColor=(0, 0, 0))
                    if formula is not None:
                        if '=' in formula:
                            message_window.error("Can't get the limit of the equation:" + str(formula))
                            continue
                        symbols = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                              'input the symbol that you use in the formula:' + str(
                                                                  formula) + ',only ONE symbol',
                                                              'OK',
                                                              'CANCEL', backgroundColor=(90, 90, 150),
                                                              promptTextColor=(0, 0, 0),
                                                              inputTextColor=(0, 0, 0))
                        symbols = sympy.symbols(symbols)
                        limit = 'None'
                        try:
                            limit = pyghelpers.textAnswerDialog(window, (200, 100, 800, 200),
                                                                'input the limit that you use in the formula:' + str(
                                                                    formula) + '(' + str(symbols) + ')',
                                                                'OK',
                                                                'CANCEL', backgroundColor=(90, 90, 150),
                                                                promptTextColor=(0, 0, 0),
                                                                inputTextColor=(0, 0, 0))
                            direction = CheckBox(3, ['+', '-', '+/-'], 1, window, clock, first_x=120, first_y=30,
                                                 each_add_x=0, each_add_y=20)
                            limit = float(limit)
                            simpified_formula = sympy.sympify(formula)
                            if type(direction.clicked_choices) == str or direction.clicked_choices == []:
                                answers = sympy.limit(simpified_formula, symbols, limit)
                            else :
                                answers = sympy.limit(simpified_formula, symbols, limit, ['+', '-', '+-'][direction.clicked_choices[0]])
                            answer = str(answers)
                            if answer == 'oo':
                                answer = 'infinity'
                            elif answer == '-oo':
                                answer = 'negative infinity'
                            elif answer == 'zoo':
                                answer = 'The limit does not exist'
                            answertext.setValue(answer)
                        except Exception as e:
                            message_window.error(
                                "Can't get the limit when" + str(symbols) + " limits to " + str(
                                    limit) + "the formula:" + formula + ", due to the Error:" + str(e))
                    else:
                        message_window.error("Failed to get the limit of the formula due to an empty formula was given")
                elif INDEX == 1:
                    MEMORY = ('', '')
                elif INDEX == 2:
                    pyperclip.copy(answer)
                elif INDEX == 3:
                    data_analyze(window, clock)
                elif INDEX == 4:
                    data_distribution(window, clock)
                elif INDEX == 5:
                    data_comparison(window, clock)
                elif INDEX == 6:
                    matrix_shower = MatrixUi(window, clock, (0, 0), 1004, 610, all_data=matrix_saved_data)
                    matrix_saved_data = matrix_shower.draw()
                event_proceeded = True
                break

        if event_proceeded:
            break
        event_proceeded = False

        if backspace.handleEvent(event):
            usr_showing_maths_texts = usr_showing_maths_texts[0:-1]
            if len(mathtext) == 0:
                continue
            while mathtext[-1] == " ":
                mathtext = mathtext[0:-1]
            mathtext = mathtext[0:-1]
            if len(mathtext) != 0:
                while mathtext[-1] == " ":
                    mathtext = mathtext[0:-1]
            if any(a in mathtext.split(" ")[-1] for a in
                   functions):  # ["sin","cos","tan",'arcsin',"arccos","arctan","log","in","root"]
                func = 1
    if point:
        line3.Buttons[0].button_is_enabled()
    else:
        line3.Buttons[0].disable()
    pygame.display.update()
    clock.tick(30)
