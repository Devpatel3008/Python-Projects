# self file was generated automatically by the Snowball to Python interpreter

from basestemmer import BaseStemmer
from among import Among


class EnglishStemmer(BaseStemmer):
    '''
    self class was automatically generated by a Snowball to Python interpreter
    It implements the stemming algorithm defined by a snowball script.
    '''
    serialVersionUID = 1

    a_0 = [
        Among(u"arsen", -1, -1),
        Among(u"commun", -1, -1),
        Among(u"gener", -1, -1)
    ]

    a_1 = [
        Among(u"'", -1, 1),
        Among(u"'s'", 0, 1),
        Among(u"'s", -1, 1)
    ]

    a_2 = [
        Among(u"ied", -1, 2),
        Among(u"s", -1, 3),
        Among(u"ies", 1, 2),
        Among(u"sses", 1, 1),
        Among(u"ss", 1, -1),
        Among(u"us", 1, -1)
    ]

    a_3 = [
        Among(u"", -1, 3),
        Among(u"bb", 0, 2),
        Among(u"dd", 0, 2),
        Among(u"ff", 0, 2),
        Among(u"gg", 0, 2),
        Among(u"bl", 0, 1),
        Among(u"mm", 0, 2),
        Among(u"nn", 0, 2),
        Among(u"pp", 0, 2),
        Among(u"rr", 0, 2),
        Among(u"at", 0, 1),
        Among(u"tt", 0, 2),
        Among(u"iz", 0, 1)
    ]

    a_4 = [
        Among(u"ed", -1, 2),
        Among(u"eed", 0, 1),
        Among(u"ing", -1, 2),
        Among(u"edly", -1, 2),
        Among(u"eedly", 3, 1),
        Among(u"ingly", -1, 2)
    ]

    a_5 = [
        Among(u"anci", -1, 3),
        Among(u"enci", -1, 2),
        Among(u"ogi", -1, 13),
        Among(u"li", -1, 16),
        Among(u"bli", 3, 12),
        Among(u"abli", 4, 4),
        Among(u"alli", 3, 8),
        Among(u"fulli", 3, 14),
        Among(u"lessli", 3, 15),
        Among(u"ousli", 3, 10),
        Among(u"entli", 3, 5),
        Among(u"aliti", -1, 8),
        Among(u"biliti", -1, 12),
        Among(u"iviti", -1, 11),
        Among(u"tional", -1, 1),
        Among(u"ational", 14, 7),
        Among(u"alism", -1, 8),
        Among(u"ation", -1, 7),
        Among(u"ization", 17, 6),
        Among(u"izer", -1, 6),
        Among(u"ator", -1, 7),
        Among(u"iveness", -1, 11),
        Among(u"fulness", -1, 9),
        Among(u"ousness", -1, 10)
    ]

    a_6 = [
        Among(u"icate", -1, 4),
        Among(u"ative", -1, 6),
        Among(u"alize", -1, 3),
        Among(u"iciti", -1, 4),
        Among(u"ical", -1, 4),
        Among(u"tional", -1, 1),
        Among(u"ational", 5, 2),
        Among(u"ful", -1, 5),
        Among(u"ness", -1, 5)
    ]

    a_7 = [
        Among(u"ic", -1, 1),
        Among(u"ance", -1, 1),
        Among(u"ence", -1, 1),
        Among(u"able", -1, 1),
        Among(u"ible", -1, 1),
        Among(u"ate", -1, 1),
        Among(u"ive", -1, 1),
        Among(u"ize", -1, 1),
        Among(u"iti", -1, 1),
        Among(u"al", -1, 1),
        Among(u"ism", -1, 1),
        Among(u"ion", -1, 2),
        Among(u"er", -1, 1),
        Among(u"ous", -1, 1),
        Among(u"ant", -1, 1),
        Among(u"ent", -1, 1),
        Among(u"ment", 15, 1),
        Among(u"ement", 16, 1)
    ]

    a_8 = [
        Among(u"e", -1, 1),
        Among(u"l", -1, 2)
    ]

    a_9 = [
        Among(u"succeed", -1, -1),
        Among(u"proceed", -1, -1),
        Among(u"exceed", -1, -1),
        Among(u"canning", -1, -1),
        Among(u"inning", -1, -1),
        Among(u"earring", -1, -1),
        Among(u"herring", -1, -1),
        Among(u"outing", -1, -1)
    ]

    a_10 = [
        Among(u"andes", -1, -1),
        Among(u"atlas", -1, -1),
        Among(u"bias", -1, -1),
        Among(u"cosmos", -1, -1),
        Among(u"dying", -1, 3),
        Among(u"early", -1, 9),
        Among(u"gently", -1, 7),
        Among(u"howe", -1, -1),
        Among(u"idly", -1, 6),
        Among(u"lying", -1, 4),
        Among(u"news", -1, -1),
        Among(u"only", -1, 10),
        Among(u"singly", -1, 11),
        Among(u"skies", -1, 2),
        Among(u"skis", -1, 1),
        Among(u"sky", -1, -1),
        Among(u"tying", -1, 5),
        Among(u"ugly", -1, 8)
    ]

    g_v = [17, 65, 16, 1]

    g_v_WXY = [1, 17, 65, 208, 1]

    g_valid_LI = [55, 141, 2]

    B_Y_found = False
    I_p2 = 0
    I_p1 = 0

    def copy_from(self, other):
        self.B_Y_found = other.B_Y_found
        self.I_p2 = other.I_p2
        self.I_p1 = other.I_p1
        super.copy_from(other)


    def r_prelude(self):
        # (, line 25
        # unset Y_found, line 26
        self.B_Y_found = False
        # do, line 27
        v_1 = self.cursor
        try:
            # (, line 27
            # [, line 27
            self.bra = self.cursor
            # literal, line 27
            if not self.eq_s(1, u"'"):
                raise lab0()
            # ], line 27
            self.ket = self.cursor
            # delete, line 27
            if not self.slice_del():
                return False

        except lab0:
            pass
        self.cursor = v_1
        # do, line 28
        v_2 = self.cursor
        try:
            # (, line 28
            # [, line 28
            self.bra = self.cursor
            # literal, line 28
            if not self.eq_s(1, u"y"):
                raise lab1()
            # ], line 28
            self.ket = self.cursor
            # <-, line 28
            if not self.slice_from(u"Y"):
                return False
            # set Y_found, line 28
            self.B_Y_found = True
        except lab1:
            pass
        self.cursor = v_2
        # do, line 29
        v_3 = self.cursor
        try:
            # repeat, line 29
            try:
                while True:
                    try:
                        v_4 = self.cursor
                        try:
                            # (, line 29
                            # goto, line 29
                            try:
                                while True:
                                    v_5 = self.cursor
                                    try:
                                        # (, line 29
                                        if not self.in_grouping(EnglishStemmer.g_v, 97, 121):
                                            raise lab7()
                                        # [, line 29
                                        self.bra = self.cursor
                                        # literal, line 29
                                        if not self.eq_s(1, u"y"):
                                            raise lab7()
                                        # ], line 29
                                        self.ket = self.cursor
                                        self.cursor = v_5
                                        raise lab6()
                                    except lab7:
                                        pass
                                    self.cursor = v_5
                                    if self.cursor >= self.limit:
                                        raise lab5()
                                    self.cursor += 1
                            except lab6:
                                pass
                            # <-, line 29
                            if not self.slice_from(u"Y"):
                                return False
                            # set Y_found, line 29
                            self.B_Y_found = True
                            raise lab4()
                        except lab5:
                            pass
                        self.cursor = v_4
                        raise lab3()
                    except lab4:
                        pass
            except lab3:
                pass
        except lab2:
            pass
        self.cursor = v_3
        return True

    def r_mark_regions(self):
        # (, line 32
        self.I_p1 = self.limit;
        self.I_p2 = self.limit;
        # do, line 35
        v_1 = self.cursor
        try:
            # (, line 35
            # or, line 41
            try:
                v_2 = self.cursor
                try:
                    # among, line 36
                    if self.find_among(EnglishStemmer.a_0, 3) == 0:
                        raise lab2()
                    raise lab1()
                except lab2:
                    pass
                self.cursor = v_2
                # (, line 41
                # gopast, line 41
                try:
                    while True:
                        try:
                            if not self.in_grouping(EnglishStemmer.g_v, 97, 121):
                                raise lab4()
                            raise lab3()
                        except lab4:
                            pass
                        if self.cursor >= self.limit:
                            raise lab0()
                        self.cursor += 1
                except lab3:
                    pass
                # gopast, line 41
                try:
                    while True:
                        try:
                            if not self.out_grouping(EnglishStemmer.g_v, 97, 121):
                                raise lab6()
                            raise lab5()
                        except lab6:
                            pass
                        if self.cursor >= self.limit:
                            raise lab0()
                        self.cursor += 1
                except lab5:
                    pass
            except lab1:
                pass
            # setmark p1, line 42
            self.I_p1 = self.cursor
            # gopast, line 43
            try:
                while True:
                    try:
                        if not self.in_grouping(EnglishStemmer.g_v, 97, 121):
                            raise lab8()
                        raise lab7()
                    except lab8:
                        pass
                    if self.cursor >= self.limit:
                        raise lab0()
                    self.cursor += 1
            except lab7:
                pass
            # gopast, line 43
            try:
                while True:
                    try:
                        if not self.out_grouping(EnglishStemmer.g_v, 97, 121):
                            raise lab10()
                        raise lab9()
                    except lab10:
                        pass
                    if self.cursor >= self.limit:
                        raise lab0()
                    self.cursor += 1
            except lab9:
                pass
            # setmark p2, line 43
            self.I_p2 = self.cursor
        except lab0:
            pass
        self.cursor = v_1
        return True

    def r_shortv(self):
        # (, line 49
        # or, line 51
        try:
            v_1 = self.limit - self.cursor
            try:
                # (, line 50
                if not self.out_grouping_b(EnglishStemmer.g_v_WXY, 89, 121):
                    raise lab1()
                if not self.in_grouping_b(EnglishStemmer.g_v, 97, 121):
                    raise lab1()
                if not self.out_grouping_b(EnglishStemmer.g_v, 97, 121):
                    raise lab1()
                raise lab0()
            except lab1:
                pass
            self.cursor = self.limit - v_1
            # (, line 52
            if not self.out_grouping_b(EnglishStemmer.g_v, 97, 121):
                return False
            if not self.in_grouping_b(EnglishStemmer.g_v, 97, 121):
                return False
            # atlimit, line 52
            if self.cursor > self.limit_backward:
                return False
        except lab0:
            pass
        return True

    def r_R1(self):
        if not self.I_p1 <= self.cursor:
            return False
        return True

    def r_R2(self):
        if not self.I_p2 <= self.cursor:
            return False
        return True

    def r_Step_1a(self):
        # (, line 58
        # try, line 59
        v_1 = self.limit - self.cursor
        try:
            # (, line 59
            # [, line 60
            self.ket = self.cursor
            # substring, line 60
            among_var = self.find_among_b(EnglishStemmer.a_1, 3)
            if among_var == 0:
                self.cursor = self.limit - v_1
                raise lab0()
            # ], line 60
            self.bra = self.cursor
            if among_var == 0:
                self.cursor = self.limit - v_1
                raise lab0()
            elif among_var == 1:
                # (, line 62
                # delete, line 62
                if not self.slice_del():
                    return False

        except lab0:
            pass
        # [, line 65
        self.ket = self.cursor
        # substring, line 65
        among_var = self.find_among_b(EnglishStemmer.a_2, 6)
        if among_var == 0:
            return False
        # ], line 65
        self.bra = self.cursor
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 66
            # <-, line 66
            if not self.slice_from(u"ss"):
                return False
        elif among_var == 2:
            # (, line 68
            # or, line 68
            try:
                v_2 = self.limit - self.cursor
                try:
                    # (, line 68
                    # hop, line 68
                    c = self.cursor - 2
                    if self.limit_backward > c or c > self.limit:
                        raise lab2()
                    self.cursor = c
                    # <-, line 68
                    if not self.slice_from(u"i"):
                        return False
                    raise lab1()
                except lab2:
                    pass
                self.cursor = self.limit - v_2
                # <-, line 68
                if not self.slice_from(u"ie"):
                    return False
            except lab1:
                pass
        elif among_var == 3:
            # (, line 69
            # next, line 69
            if self.cursor <= self.limit_backward:
                return False
            self.cursor -= 1
            # gopast, line 69
            try:
                while True:
                    try:
                        if not self.in_grouping_b(EnglishStemmer.g_v, 97, 121):
                            raise lab4()
                        raise lab3()
                    except lab4:
                        pass
                    if self.cursor <= self.limit_backward:
                        return False
                    self.cursor -= 1
            except lab3:
                pass
            # delete, line 69
            if not self.slice_del():
                return False

        return True

    def r_Step_1b(self):
        # (, line 74
        # [, line 75
        self.ket = self.cursor
        # substring, line 75
        among_var = self.find_among_b(EnglishStemmer.a_4, 6)
        if among_var == 0:
            return False
        # ], line 75
        self.bra = self.cursor
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 77
            # call R1, line 77
            if not self.r_R1():
                return False
            # <-, line 77
            if not self.slice_from(u"ee"):
                return False
        elif among_var == 2:
            # (, line 79
            # test, line 80
            v_1 = self.limit - self.cursor
            # gopast, line 80
            try:
                while True:
                    try:
                        if not self.in_grouping_b(EnglishStemmer.g_v, 97, 121):
                            raise lab1()
                        raise lab0()
                    except lab1:
                        pass
                    if self.cursor <= self.limit_backward:
                        return False
                    self.cursor -= 1
            except lab0:
                pass
            self.cursor = self.limit - v_1
            # delete, line 80
            if not self.slice_del():
                return False

            # test, line 81
            v_3 = self.limit - self.cursor
            # substring, line 81
            among_var = self.find_among_b(EnglishStemmer.a_3, 13)
            if among_var == 0:
                return False
            self.cursor = self.limit - v_3
            if among_var == 0:
                return False
            elif among_var == 1:
                # (, line 83
                # <+, line 83
                c = self.cursor
                self.insert(self.cursor, self.cursor, u"e")
                self.cursor = c
            elif among_var == 2:
                # (, line 86
                # [, line 86
                self.ket = self.cursor
                # next, line 86
                if self.cursor <= self.limit_backward:
                    return False
                self.cursor -= 1
                # ], line 86
                self.bra = self.cursor
                # delete, line 86
                if not self.slice_del():
                    return False

            elif among_var == 3:
                # (, line 87
                # atmark, line 87
                if self.cursor != self.I_p1:
                    return False
                # test, line 87
                v_4 = self.limit - self.cursor
                # call shortv, line 87
                if not self.r_shortv():
                    return False
                self.cursor = self.limit - v_4
                # <+, line 87
                c = self.cursor
                self.insert(self.cursor, self.cursor, u"e")
                self.cursor = c
        return True

    def r_Step_1c(self):
        # (, line 93
        # [, line 94
        self.ket = self.cursor
        # or, line 94
        try:
            v_1 = self.limit - self.cursor
            try:
                # literal, line 94
                if not self.eq_s_b(1, u"y"):
                    raise lab1()
                raise lab0()
            except lab1:
                pass
            self.cursor = self.limit - v_1
            # literal, line 94
            if not self.eq_s_b(1, u"Y"):
                return False
        except lab0:
            pass
        # ], line 94
        self.bra = self.cursor
        if not self.out_grouping_b(EnglishStemmer.g_v, 97, 121):
            return False
        # not, line 95
        v_2 = self.limit - self.cursor
        try:
            # atlimit, line 95
            if self.cursor > self.limit_backward:
                raise lab2()
            return False
        except lab2:
            pass
        self.cursor = self.limit - v_2
        # <-, line 96
        if not self.slice_from(u"i"):
            return False
        return True

    def r_Step_2(self):
        # (, line 99
        # [, line 100
        self.ket = self.cursor
        # substring, line 100
        among_var = self.find_among_b(EnglishStemmer.a_5, 24)
        if among_var == 0:
            return False
        # ], line 100
        self.bra = self.cursor
        # call R1, line 100
        if not self.r_R1():
            return False
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 101
            # <-, line 101
            if not self.slice_from(u"tion"):
                return False
        elif among_var == 2:
            # (, line 102
            # <-, line 102
            if not self.slice_from(u"ence"):
                return False
        elif among_var == 3:
            # (, line 103
            # <-, line 103
            if not self.slice_from(u"ance"):
                return False
        elif among_var == 4:
            # (, line 104
            # <-, line 104
            if not self.slice_from(u"able"):
                return False
        elif among_var == 5:
            # (, line 105
            # <-, line 105
            if not self.slice_from(u"ent"):
                return False
        elif among_var == 6:
            # (, line 107
            # <-, line 107
            if not self.slice_from(u"ize"):
                return False
        elif among_var == 7:
            # (, line 109
            # <-, line 109
            if not self.slice_from(u"ate"):
                return False
        elif among_var == 8:
            # (, line 111
            # <-, line 111
            if not self.slice_from(u"al"):
                return False
        elif among_var == 9:
            # (, line 112
            # <-, line 112
            if not self.slice_from(u"ful"):
                return False
        elif among_var == 10:
            # (, line 114
            # <-, line 114
            if not self.slice_from(u"ous"):
                return False
        elif among_var == 11:
            # (, line 116
            # <-, line 116
            if not self.slice_from(u"ive"):
                return False
        elif among_var == 12:
            # (, line 118
            # <-, line 118
            if not self.slice_from(u"ble"):
                return False
        elif among_var == 13:
            # (, line 119
            # literal, line 119
            if not self.eq_s_b(1, u"l"):
                return False
            # <-, line 119
            if not self.slice_from(u"og"):
                return False
        elif among_var == 14:
            # (, line 120
            # <-, line 120
            if not self.slice_from(u"ful"):
                return False
        elif among_var == 15:
            # (, line 121
            # <-, line 121
            if not self.slice_from(u"less"):
                return False
        elif among_var == 16:
            # (, line 122
            if not self.in_grouping_b(EnglishStemmer.g_valid_LI, 99, 116):
                return False
            # delete, line 122
            if not self.slice_del():
                return False

        return True

    def r_Step_3(self):
        # (, line 126
        # [, line 127
        self.ket = self.cursor
        # substring, line 127
        among_var = self.find_among_b(EnglishStemmer.a_6, 9)
        if among_var == 0:
            return False
        # ], line 127
        self.bra = self.cursor
        # call R1, line 127
        if not self.r_R1():
            return False
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 128
            # <-, line 128
            if not self.slice_from(u"tion"):
                return False
        elif among_var == 2:
            # (, line 129
            # <-, line 129
            if not self.slice_from(u"ate"):
                return False
        elif among_var == 3:
            # (, line 130
            # <-, line 130
            if not self.slice_from(u"al"):
                return False
        elif among_var == 4:
            # (, line 132
            # <-, line 132
            if not self.slice_from(u"ic"):
                return False
        elif among_var == 5:
            # (, line 134
            # delete, line 134
            if not self.slice_del():
                return False

        elif among_var == 6:
            # (, line 136
            # call R2, line 136
            if not self.r_R2():
                return False
            # delete, line 136
            if not self.slice_del():
                return False

        return True

    def r_Step_4(self):
        # (, line 140
        # [, line 141
        self.ket = self.cursor
        # substring, line 141
        among_var = self.find_among_b(EnglishStemmer.a_7, 18)
        if among_var == 0:
            return False
        # ], line 141
        self.bra = self.cursor
        # call R2, line 141
        if not self.r_R2():
            return False
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 144
            # delete, line 144
            if not self.slice_del():
                return False

        elif among_var == 2:
            # (, line 145
            # or, line 145
            try:
                v_1 = self.limit - self.cursor
                try:
                    # literal, line 145
                    if not self.eq_s_b(1, u"s"):
                        raise lab1()
                    raise lab0()
                except lab1:
                    pass
                self.cursor = self.limit - v_1
                # literal, line 145
                if not self.eq_s_b(1, u"t"):
                    return False
            except lab0:
                pass
            # delete, line 145
            if not self.slice_del():
                return False

        return True

    def r_Step_5(self):
        # (, line 149
        # [, line 150
        self.ket = self.cursor
        # substring, line 150
        among_var = self.find_among_b(EnglishStemmer.a_8, 2)
        if among_var == 0:
            return False
        # ], line 150
        self.bra = self.cursor
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 151
            # or, line 151
            try:
                v_1 = self.limit - self.cursor
                try:
                    # call R2, line 151
                    if not self.r_R2():
                        raise lab1()
                    raise lab0()
                except lab1:
                    pass
                self.cursor = self.limit - v_1
                # (, line 151
                # call R1, line 151
                if not self.r_R1():
                    return False
                # not, line 151
                v_2 = self.limit - self.cursor
                try:
                    # call shortv, line 151
                    if not self.r_shortv():
                        raise lab2()
                    return False
                except lab2:
                    pass
                self.cursor = self.limit - v_2
            except lab0:
                pass
            # delete, line 151
            if not self.slice_del():
                return False

        elif among_var == 2:
            # (, line 152
            # call R2, line 152
            if not self.r_R2():
                return False
            # literal, line 152
            if not self.eq_s_b(1, u"l"):
                return False
            # delete, line 152
            if not self.slice_del():
                return False

        return True

    def r_exception2(self):
        # (, line 156
        # [, line 158
        self.ket = self.cursor
        # substring, line 158
        if self.find_among_b(EnglishStemmer.a_9, 8) == 0:
            return False
        # ], line 158
        self.bra = self.cursor
        # atlimit, line 158
        if self.cursor > self.limit_backward:
            return False
        return True

    def r_exception1(self):
        # (, line 168
        # [, line 170
        self.bra = self.cursor
        # substring, line 170
        among_var = self.find_among(EnglishStemmer.a_10, 18)
        if among_var == 0:
            return False
        # ], line 170
        self.ket = self.cursor
        # atlimit, line 170
        if self.cursor < self.limit:
            return False
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 174
            # <-, line 174
            if not self.slice_from(u"ski"):
                return False
        elif among_var == 2:
            # (, line 175
            # <-, line 175
            if not self.slice_from(u"sky"):
                return False
        elif among_var == 3:
            # (, line 176
            # <-, line 176
            if not self.slice_from(u"die"):
                return False
        elif among_var == 4:
            # (, line 177
            # <-, line 177
            if not self.slice_from(u"lie"):
                return False
        elif among_var == 5:
            # (, line 178
            # <-, line 178
            if not self.slice_from(u"tie"):
                return False
        elif among_var == 6:
            # (, line 182
            # <-, line 182
            if not self.slice_from(u"idl"):
                return False
        elif among_var == 7:
            # (, line 183
            # <-, line 183
            if not self.slice_from(u"gentl"):
                return False
        elif among_var == 8:
            # (, line 184
            # <-, line 184
            if not self.slice_from(u"ugli"):
                return False
        elif among_var == 9:
            # (, line 185
            # <-, line 185
            if not self.slice_from(u"earli"):
                return False
        elif among_var == 10:
            # (, line 186
            # <-, line 186
            if not self.slice_from(u"onli"):
                return False
        elif among_var == 11:
            # (, line 187
            # <-, line 187
            if not self.slice_from(u"singl"):
                return False
        return True

    def r_postlude(self):
        # (, line 203
        # Boolean test Y_found, line 203
        if not self.B_Y_found:
            return False
        # repeat, line 203
        try:
            while True:
                try:
                    v_1 = self.cursor
                    try:
                        # (, line 203
                        # goto, line 203
                        try:
                            while True:
                                v_2 = self.cursor
                                try:
                                    # (, line 203
                                    # [, line 203
                                    self.bra = self.cursor
                                    # literal, line 203
                                    if not self.eq_s(1, u"Y"):
                                        raise lab4()
                                    # ], line 203
                                    self.ket = self.cursor
                                    self.cursor = v_2
                                    raise lab3()
                                except lab4:
                                    pass
                                self.cursor = v_2
                                if self.cursor >= self.limit:
                                    raise lab2()
                                self.cursor += 1
                        except lab3:
                            pass
                        # <-, line 203
                        if not self.slice_from(u"y"):
                            return False
                        raise lab1()
                    except lab2:
                        pass
                    self.cursor = v_1
                    raise lab0()
                except lab1:
                    pass
        except lab0:
            pass
        return True

    def _stem(self):
        # (, line 205
        # or, line 207
        try:
            v_1 = self.cursor
            try:
                # call exception1, line 207
                if not self.r_exception1():
                    raise lab1()
                raise lab0()
            except lab1:
                pass
            self.cursor = v_1
            try:
                # not, line 208
                v_2 = self.cursor
                try:
                    # hop, line 208
                    c = self.cursor + 3
                    if 0 > c or c > self.limit:
                        raise lab3()
                    self.cursor = c
                    raise lab2()
                except lab3:
                    pass
                self.cursor = v_2
                raise lab0()
            except lab2:
                pass
            self.cursor = v_1
            # (, line 208
            # do, line 209
            v_3 = self.cursor
            try:
                # call prelude, line 209
                if not self.r_prelude():
                    raise lab4()
            except lab4:
                pass
            self.cursor = v_3
            # do, line 210
            v_4 = self.cursor
            try:
                # call mark_regions, line 210
                if not self.r_mark_regions():
                    raise lab5()
            except lab5:
                pass
            self.cursor = v_4
            # backwards, line 211
            self.limit_backward = self.cursor
            self.cursor = self.limit
            # (, line 211
            # do, line 213
            v_5 = self.limit - self.cursor
            try:
                # call Step_1a, line 213
                if not self.r_Step_1a():
                    raise lab6()
            except lab6:
                pass
            self.cursor = self.limit - v_5
            # or, line 215
            try:
                v_6 = self.limit - self.cursor
                try:
                    # call exception2, line 215
                    if not self.r_exception2():
                        raise lab8()
                    raise lab7()
                except lab8:
                    pass
                self.cursor = self.limit - v_6
                # (, line 215
                # do, line 217
                v_7 = self.limit - self.cursor
                try:
                    # call Step_1b, line 217
                    if not self.r_Step_1b():
                        raise lab9()
                except lab9:
                    pass
                self.cursor = self.limit - v_7
                # do, line 218
                v_8 = self.limit - self.cursor
                try:
                    # call Step_1c, line 218
                    if not self.r_Step_1c():
                        raise lab10()
                except lab10:
                    pass
                self.cursor = self.limit - v_8
                # do, line 220
                v_9 = self.limit - self.cursor
                try:
                    # call Step_2, line 220
                    if not self.r_Step_2():
                        raise lab11()
                except lab11:
                    pass
                self.cursor = self.limit - v_9
                # do, line 221
                v_10 = self.limit - self.cursor
                try:
                    # call Step_3, line 221
                    if not self.r_Step_3():
                        raise lab12()
                except lab12:
                    pass
                self.cursor = self.limit - v_10
                # do, line 222
                v_11 = self.limit - self.cursor
                try:
                    # call Step_4, line 222
                    if not self.r_Step_4():
                        raise lab13()
                except lab13:
                    pass
                self.cursor = self.limit - v_11
                # do, line 224
                v_12 = self.limit - self.cursor
                try:
                    # call Step_5, line 224
                    if not self.r_Step_5():
                        raise lab14()
                except lab14:
                    pass
                self.cursor = self.limit - v_12
            except lab7:
                pass
            self.cursor = self.limit_backward
            # do, line 227
            v_13 = self.cursor
            try:
                # call postlude, line 227
                if not self.r_postlude():
                    raise lab15()
            except lab15:
                pass
            self.cursor = v_13
        except lab0:
            pass
        return True

    def equals(self, o):
        return isinstance(o, EnglishStemmer)

    def hashCode(self):
        return hash("EnglishStemmer")


class lab0(BaseException): pass


class lab1(BaseException): pass


class lab2(BaseException): pass


class lab3(BaseException): pass


class lab4(BaseException): pass


class lab5(BaseException): pass


class lab6(BaseException): pass


class lab7(BaseException): pass


class lab8(BaseException): pass


class lab9(BaseException): pass


class lab10(BaseException): pass


class lab11(BaseException): pass


class lab12(BaseException): pass


class lab13(BaseException): pass


class lab14(BaseException): pass


class lab15(BaseException): pass
