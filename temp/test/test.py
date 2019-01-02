import hug

def start(api):

  def tested():
    return "Yeahhhh!!!!"

  hug.get('/work', api=api)(tested)
