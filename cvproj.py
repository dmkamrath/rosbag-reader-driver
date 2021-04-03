import re
import sys
import os

# Regex

PROJECT_NAME_RE = "^set *\\(PROJECT_NAME \\w*\\)"

TEMPLATE_MAIN_REPLACE = "unnamed"

def get_cmake_project_name_replacement(new_project_name):
	return 'set(PROJECT_NAME {})\n'.format(new_project_name)

# Parameter getters

def get_proj_root_name():
	return 'cvproj'

def get_proj_root_path():
	return os.path.join('../', get_proj_root_name())

def get_proj_root_rename_path(new_name):
	return os.path.join('../', new_name)

def get_cmakelists_path():
	return 'CMakeLists.txt'

def get_template_main_name():
	return 'unnamed.cpp'

def get_src_path():
	return 'src'

def get_template_main_path():
	return os.path.join(get_src_path(), get_template_main_name())

def get_template_rename_path(new_name):
	return os.path.join(get_src_path(), new_name)

def check_line_re_match(line, regex):
	m = re.findall(regex, line)
	return len(m) > 0

# File IO

def read_f(fname):
	with open(fname) as f:
		return f.readlines()

def write_f(fname, lines):
	with open(fname, 'w') as f:
		for l in lines:
			f.write(l)

def fe(fname):
	return os.path.isfile(fname)

def rm_if_exists(fname):
	if fe(fname):
		os.remove(fname)

# File Manip

def replace_matching_lines(lines, regex, replacement):
	for i in range(len(lines)):
		if check_line_re_match(lines[i], regex):
			lines[i] = replacement

def replace_matching_string_in_lines(lines, string, replacement):
	for i in range(len(lines)):
		if string in lines[i]:
			lines[i] = lines[i].replace(string, replacement)

def replace_file_lines(fname, regex, replacement):
	lines = read_f(fname)
	replace_matching_lines(lines, regex, replacement)
	write_f(fname, lines)

def replace_file_strings(fname, string, replacement):
	lines = read_f(fname)
	replace_matching_string_in_lines(lines, string, replacement)
	write_f(fname, lines)

def set_cmake_project_name(lines, new_project_name):
	for i in range(len(lines)):
		if check_line_re_match(lines[i], PROJECT_NAME_RE):
			lines[i] = 'set(PROJECT_NAME {})\n'.format(new_project_name)

def change_cmake_project_name(new_project_name):
	replace_file_lines(get_cmakelists_path(), PROJECT_NAME_RE, get_cmake_project_name_replacement(new_project_name))

def set_template_main_fname(new_name):
	os.rename(get_template_main_path(), get_template_rename_path(new_name))

def set_template_main_gencode_names(new_name):
	replace_file_strings(get_template_main_path(), TEMPLATE_MAIN_REPLACE, new_name)\

def rename_proj_root_dir(new_name):
	os.rename(get_proj_root_path(), get_proj_root_rename_path(new_name))

def change_project_name(new_name):
	change_cmake_project_name(new_name)
	set_template_main_gencode_names(new_name)
	set_template_main_fname(new_name + '.cpp')
	rename_proj_root_dir(new_name)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		quit()

	proj_name = sys.argv[1]
	change_project_name(proj_name)