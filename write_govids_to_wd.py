import psycopg2
import pywikibot

conn = psycopg2.connect(DBAUTH)

site = pywikibot.Site('wikidata') 
repo = site.data_repository()
wd_prop_gov_id = 'P2503'


def select_refs(startwdid):
    cursor = conn.cursor()
    sql = "select wd_id, gov_id from refs_wd_gov where wd_id>='" + startwdid + "' order by wd_id"
    cursor.execute(sql);
    result = cursor.fetchall()
    for row in result:
        wd_id = row[0]
        gov_id = row[1]
        write_to_wikidata(wd_id, gov_id)
 

def write_to_wikidata(wd_id, gov_id):
    try:
        item = pywikibot.ItemPage(repo, wd_id) 
        item.get()

        if wd_prop_gov_id in item.claims:
            print("INFO: ALREADY SET: " + wd_prop_gov_id + " for wd item " + wd_id + " - value: " + item.claims[wd_prop_gov_id][0].getTarget())
        
        else:
            claim = pywikibot.Claim(repo, wd_prop_gov_id)
            claim.setTarget(gov_id)
            item.addClaim(claim, summary=u'Adding id of appropriate GOV entity')
            print("INFO: SET BY BOT: " + wd_prop_gov_id + " for wd item " + wd_id + " - value: " + gov_id)

    except Exception as e:
        print()
        print("ERROR: ACCESS/WRITE FAILED: to wd item " + wd_id)
        print(e)
        print()


select_refs('0')
