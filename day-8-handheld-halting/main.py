from data import DATA
from cpu import CPU, InfiniteLoopError
from pprint import pprint
from sys import exit

class RecoveryError(Exception):
    pass

class CorrectingCPU(CPU):

    def __init__(self, instructions=None, debug=False, detect_loop=False):
        super().__init__(instructions=instructions, debug=debug, detect_loop=detect_loop)
        self.detect_loop = True
        self.saves = []

    def run(self):
        if self.debug:
            print('state\tpc\tir\tacc\top\targ\tloops')
            print('-----\t-----\t-----\t-----\t-----\t-----\t-----')
            self._print_debug('START')

        fail = False

        while not fail:
            try:
                self._fetch()
                self._decode()

                try:
                    self._execute()
                except InfiniteLoopError:
                    try:
                        self._recover()
                        self._execute(ignore_loop=True)
                    except (RecoveryError, InfiniteLoopError):
                        fail = True
            except IndexError:
                return self._exit()

    def _save(self):
        """Save current state to be restored later."""
        save = (self.pc, self.ir, self.acc, self.history) # Decrement PC to account for increment in fetch step
        self.saves.append(save)
        return save

    def _recover(self):
        """Restore previously saved state"""
        try:
            pc, ir, acc, history = self.saves.pop()
        except IndexError:
            # Save stack is empty. No recovery possible.
            if self.debug:
                self._print_debug('FAIL')
            raise RecoveryError
        
        self.pc = pc
        self.ir = ir
        self.acc = acc
        self.history = history

        super()._decode()
        self.op = 'jmp' if self.op == 'nop' else 'nop'

    def _decode(self):
        op, arg = super()._decode()

        if op == 'jmp' or op == 'nop':
            # Store something in stack to be returned to later
            self._save()

        return op, arg

instructions = DATA.splitlines()

if __name__ == "__main__":
    # cpu = CPU(instructions, debug=True, detect_loop=True)
    cpu = CorrectingCPU(instructions, debug=True, detect_loop=True)

    # cpu.pc = 8

    cpu.run()




