from flask import Flask, render_template, request
import config_pb2
import struct

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
    print whole_pb
    rule = config_pb2.AuditRule()
    rule.id = 1
    rule.filter = "Always == True"
    field1 = rule.field.add()
    field1 = metric_1
    field2 = rule.field.add()
    field2 = metric_2
    rule.field.extend([metric_1,metric_2])
    print rule
    whole_pb.auditRules = whole_pb.auditRules.add()
    whole_pb.auditRules.extend([rule])
    f = open("res", "wb")
    f.write(whole_pb.SerializeToString())
    f.close()

@app.route('/', methods=['POST', 'GET"'])
def my_form_post():
    metric_1 = request.form['mt1']
    metric_2 = request.form['mt2']
    fil = request.form['fil']
    operator = request.form['op']
    val = request.form['val']
    print metric_1, metric_2, fil, operator, val
    edit_protobuf(metric_1, metric_2, fil, operator, val)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)