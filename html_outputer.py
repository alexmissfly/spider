class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.data.append(new_data)


    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.write("<meta charset='utf-8'>")

        for data in self.data:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        pass
