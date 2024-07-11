import cmd

class MyCommandInterpreter(cmd.Cmd):
    prompt = '(my_interpreter) '
    intro = 'Welcome to My Command Interpreter. Type help or ? to list commands.\n'

    def do_greet(self, arg):
        """Greet the user"""
        print(f"Hello, {arg}!")
    
    def do_sum(self, arg):
        nums = arg.split()
        print(nums)
        originNum = list(map(int, nums))
        print(originNum)
        result = sum(originNum)
        print(result)

    def do_exit(self, arg):
        """Exit the interpreter"""
        print("Goodbye!")
        return True

    def cmdloop(self, intro=None):
        print("Starting the command loop. Type 'exit' to quit.")
        super().cmdloop(intro)

if __name__ == '__main__':
    MyCommandInterpreter().cmdloop()
