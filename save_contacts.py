from selenium import webdriver
from time import sleep
import os
webscript1='''



const moduleRaid = function () {
  moduleRaid.mID  = Math.random().toString(36).substring(7);
  moduleRaid.mObj = {};

  fillModuleArray = function() {
    (window.webpackChunkbuild || window.webpackChunkwhatsapp_web_client).push([
      [moduleRaid.mID], {}, function(e) {
        Object.keys(e.m).forEach(function(mod) {
          moduleRaid.mObj[mod] = e(mod);
        })
      }
    ]);
  }

  fillModuleArray();

  get = function get (id) {
    return moduleRaid.mObj[id]
  }

  findModule = function findModule (query) {
    results = [];
    modules = Object.keys(moduleRaid.mObj);

    modules.forEach(function(mKey) {
      mod = moduleRaid.mObj[mKey];

      if (typeof mod !== 'undefined') {
        if (typeof query === 'string') {
          if (typeof mod.default === 'object') {
            for (key in mod.default) {
              if (key == query) results.push(mod);
            }
          }

          for (key in mod) {
            if (key == query) results.push(mod);
          }
        } else if (typeof query === 'function') { 
          if (query(mod)) {
            results.push(mod);
          }
        } else {
          throw new TypeError('findModule can only find via string and function, ' + (typeof query) + ' was passed');
        }
        
      }
    })

    return results;
  }

  return {
    modules: moduleRaid.mObj,
    constructors: moduleRaid.cArr,
    findModule: findModule,
    get: get
  }
}

if (typeof module === 'object' && module.exports) {
  module.exports = moduleRaid;
} else {
  window.mR = moduleRaid();
}
window.mR = moduleRaid();
window.Store = Object.assign({}, window.mR.findModule(m => m.default && m.default.Chat)[0].default);




'''
webscript2='''

function startnew(){

var parentWindow ;

window.Store.Chat.toArray().forEach(function(c) {
if (!c || !c.id)
return;

if (c.isGroup)
return;
if (c.contact.isAddressBookContact==1)
return;

console.log(c.id+ '');
	});		
		
	}		
startnew();


'''


cwd=os.getcwd()


    
options = webdriver.ChromeOptions() 
options.add_argument(f"user-data-dir={cwd}\\whatsapp")
options.set_capability("goog:loggingPrefs",{ 'browser':'ALL' })
driver = webdriver.Chrome(options=options)
driver.get ("https://web.whatsapp.com")
input("Press Enter after scanning QR code...")
sleep(30)
driver.execute_script(webscript1)


L=[]
driver.execute_script(webscript2)
for e in driver.get_log('browser'):
  numberline=e['message']

  numberphrase=numberline.split(' ')[2]

  modnumberphrase=numberphrase.replace('"','')
  Modnumberphrase=modnumberphrase.replace('"','')

  number=Modnumberphrase.split('@')[0]

  L.append(number)
with open('google_contacts.csv','w') as f:
        f.write(f'Name,Phone\n')
        
        for i in L:
            if i.isdigit():
                print(i)
                f.write(f'{i},+{i}\n') 