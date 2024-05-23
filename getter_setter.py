class my_class:
    def __int__(self,value):
        self._value=value
    
    def show(self):
        print(f'the value is {self._value}')
    
    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def tem_value(self,new_value):
        self._value=new_value/10

obj=my_class(10)
print(obj.value)
obj.value=67
obj.show() 