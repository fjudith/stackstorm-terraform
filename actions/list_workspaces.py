import os
from lib import action

class ListWorkspaces(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec):
        """
        List Terraform workspaces

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform workspace list command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.workspace("list", planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)