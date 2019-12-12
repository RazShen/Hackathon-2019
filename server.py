from flask import Flask, render_template, request
import config_pb2
import os
app = Flask(__name__, template_folder=".",static_url_path='/static')


@app.route('/')
def home():
    return render_template('index.html')

def edit_protobuf(metric_1, metric_2, fil, operator, val):
    ex_f = open("955944.pb", "rb")
    buf = ex_f.read()
    ex_f.close()
    whole_pb = config_pb2.SiteConfig()
    whole_pb.ParseFromString(buf)
    rule = config_pb2.AuditRule()
    rule.id = 7
    rule.name = b"Hackathon Cool"
    rule.filter =b"Always == True"
    rule.field[:] = [metric_1.encode(), metric_2.encode()]
    whole_pb.siteRulesConf.auditRules.append(rule)
    f = open("res", "wb")
    f.write(whole_pb.SerializeToString())
    f.close()
    os.system("curl -k -X POST --data-binary @/Users/raz.shenkman/Documents/hackathon_2019/res 198.143.43.201/_Incapsula_Resource?XMSHLOMIT=955944")

@app.route('/', methods=['POST', 'GET"'])
def my_form_post():
    metric_1 = request.form['mt1']
    metric_2 = request.form['mt2']
    fil = request.form['fil']
    operator = request.form['op']
    val = request.form['val']
    edit_protobuf(metric_1, metric_2, fil, operator, val)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)