import os

palette_output_txt_path = os.path.join('gen_palette_output.txt')

total_color_type = 59
total_grade = 4
palette_grade_list = []


# 得到调色盘的所有登记
def get_palette_grade():
    per_grade_cnt = int(255 / total_grade)
    for i in range(total_grade - 1):
        palette_grade_list.append(i * per_grade_cnt)

    palette_grade_list.append(255)


def gen_palette_by_txt():
    with open(palette_output_txt_path, 'w') as f:
        r_list = palette_grade_list.copy()
        g_list = palette_grade_list.copy()
        b_list = palette_grade_list.copy()

        output_str = '['
        i = 0

        for r in r_list:
            for g in g_list:
                for b in b_list:
                    rgb_out = f'[{r},{g},{b}]'
                    output_str += rgb_out
                    i += 1
                    if i < total_color_type:
                        output_str += ','
                    else:
                        output_str += ']'
                        print(output_str)
                        f.writelines(output_str)
                        return


if __name__ == '__main__':
    get_palette_grade()
    gen_palette_by_txt()
