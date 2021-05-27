from multiprocessing.pool import ThreadPool
import win32file
import win32pipe

class Piper:
  PLUGIN_PIPE_SIZE = 512 

  def __init__(self):
    self._pipe = None
    self._connected = False

  @staticmethod
  def format_pipe_id(pipe_id):
      return r"\\.\pipe\{}".format(pipe_id)

  # Dont change pipe_name, Not implemented yet
  def open_pipe(self, pipe_name='field_set_pipe', num_allowed_instances=1):
      self._connected = False

      pool = ThreadPool(processes=1)

      self._pipe = win32pipe.CreateNamedPipe(Piper.format_pipe_id(pipe_name),
                                             win32pipe.PIPE_ACCESS_DUPLEX | win32file.FILE_FLAG_OVERLAPPED,

                                             win32pipe.PIPE_TYPE_MESSAGE |
                                             win32pipe.PIPE_READMODE_MESSAGE |
                                             win32pipe.PIPE_WAIT,

                                             # num_allowed_instances,

                                             win32pipe.PIPE_UNLIMITED_INSTANCES,

                                             Piper.PLUGIN_PIPE_SIZE,
                                             Piper.PLUGIN_PIPE_SIZE, 0, None)

      win32pipe.ConnectNamedPipe(self._pipe)

      self._connected = True

      pool.terminate()
      pool.join()

  def write_pipe(self, message):
    win32file.WriteFile(self._pipe, str.encode(message + '\0'))
