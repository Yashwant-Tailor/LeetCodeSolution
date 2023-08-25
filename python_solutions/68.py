class Solution:
    def get_next_line(self,words,maxWidth,idx):
        curr_len = 0
        word_cnt = 0
        line_words = []
        while idx < len(words) and curr_len + len(words[idx]) <= maxWidth:
            line_words.append(words[idx])
            word_cnt += 1
            curr_len += len(words[idx])
            curr_len += 1 # space
            idx += 1
        line_status = "NOT_LAST_LINE"
        if idx == len(words):
            line_status = "LAST_LINE"
        return line_status,idx,line_words
    def get_char_cnt(self,line_words):
        ans = 0
        for word in line_words:
            ans += len(word)
        return ans
    def get_space_str(self,space_cnt):
        st = ''
        for i in range(space_cnt):
            st += ' '
        return st
    def justify_text(self,line_words,maxWidth):
        if len(line_words) == 1:
            line_words.append('')
        text = ""
        char_cnt = self.get_char_cnt(line_words)
        len_words = len(line_words)
        space_between_words = (maxWidth-char_cnt)//(len_words-1)
        extra_space = (maxWidth-char_cnt)%(len_words-1)
        space_str = self.get_space_str(space_between_words)
        for idx,word in enumerate(line_words):
            if idx > 0:
                text += space_str
                if extra_space > 0:
                    text += ' '
                    extra_space -= 1
            text += word
        return text
    def left_justify(self,line_words,maxWidth):
        curr_len = 0
        text = ""
        for idx,word in enumerate(line_words):
            if idx > 0:
                text += " "
                curr_len += 1
            text += word
            curr_len += len(word)
        text += self.get_space_str(maxWidth-curr_len)
        return text

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Solution Overview
        # just do as mention in the problem statement
        text = []
        curr_line_words = []
        idx = 0
        while True:
            line_status,idx,curr_line_words = self.get_next_line(words,maxWidth,idx)
            if line_status == "LAST_LINE":
                text.append(self.left_justify(curr_line_words,maxWidth))
                break
            else:
                text.append(self.justify_text(curr_line_words,maxWidth))
        return text
