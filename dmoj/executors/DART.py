from dmoj.executors.compiled_executor import CompiledExecutor


# Running DART normally results in unholy memory usage
# Thankfully compiling it results in something...far more sane
class Executor(CompiledExecutor):
    ext = 'dart'
    name = 'DART'
    nproc = -1  # Dart uses a really, really large number of threads
    command = 'dart'
    test_program = """
void main() {
    print("echo: Hello, World!");
}
"""
    address_grace = 128 * 1024

    syscalls = ['epoll_create', 'epoll_ctl', 'epoll_wait', 'timerfd_settime', 'memfd_create', 'ftruncate']

    def get_compile_args(self):
        return [self.get_command(), '--snapshot=%s' % self.get_compiled_file(), self._code]

    def get_cmdline(self, **kwargs):
        return [self.get_command(), self.get_compiled_file()]

    def get_executable(self):
        return self.get_command()
