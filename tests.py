from functions.get_files_info import get_files_info
import unittest



class TestGetFilesInfo(unittest.TestCase):
    def test_case1(self):
        result = get_files_info("calculator", ".")
        self.assertEqual(
            result, 
            "- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False\n")
        
    def test_case2(self):
        result = get_files_info("calculator", "pkg")
        self.assertEqual(
            result, 
            "- calculator.py: file_size=1737 bytes, is_dir=False\n- render.py: file_size=766 bytes, is_dir=False\n")
   
    def test_case3(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result,'Error: Cannot list "/bin" as it is outside the permitted working directory')
                
    def test_case4(self):        
        result = get_files_info("calculator", "../")
        self.assertEqual(
            result, 
            'Error: Cannot list "../" as it is outside the permitted working directory')
        

if __name__ == "__main__":
    unittest.main()