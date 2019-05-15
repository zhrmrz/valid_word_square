class Sol:
    def valid_word_square(self,list):
        l=list[0]
        arr=[]
        for i in range(len(l)):
            for j in range(len(l)):
                if list[j].startswith(l[i]):
                    arr.append(list[i])
                    break
        if len(list)==len(arr):
            return True
        return False

if __name__ == '__main__':
    p1=Sol()
    print(p1.valid_word_square(['cool','lead','lady','area']))
