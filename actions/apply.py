from lib import action
import os

class Apply(action.BaseAction):
    def run(self, planpath, variable_files):
      os.chdir(planpath)
      return_code, stdout, stderr =  self.terraform.apply(planpath, var_file=variable_files)
      output = stdout + "\n" + stderr
      if return_code == 0:
        return (True, output)
      else:
	    return (False, output)
