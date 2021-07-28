def Audit(doc_obj, path):
    section = doc_obj.sections[0].first_page_header
    for par in section.paragraphs:
        if 'graphicData' in par._p.xml:
            if par._p.xml.count('graphicData') > 2:
                print(par._p.xml.count('graphicData'), 'Images')
                par.runs[0].clear()
        doc_obj.save(path)
