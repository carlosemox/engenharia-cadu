const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'docs/fabrica/routes.json'),'utf8'));
const nodes={};
for(const id of ['status','mode','target','request','attachment','output','copy'])nodes[id]={value:'',textContent:'',checked:false,events:{},addEventListener(e,f){this.events[e]=f},focus(){},select(){this.selected=true}};
nodes.mode.value='auto';let clipboard='';
const context={document:{getElementById:id=>nodes[id]},fetch:async()=>({ok:true,json:async()=>catalog}),navigator:{clipboard:{writeText:async text=>{clipboard=text}}}};
vm.runInNewContext(fs.readFileSync(path.join(root,'docs/assets/factory.js'),'utf8'),context);
setImmediate(async()=>{
 try{
  nodes.target.value='repo "x" <script>no()</script>';
  nodes.request.value="Preservar $& $$ $` $'\ntexto";nodes.attachment.checked=true;
  for(const mode of Object.keys(catalog.routes)){
   nodes.mode.value=mode;nodes.mode.events.input();
   const data=JSON.parse(nodes.output.value.split('adicional):\n')[1].split('\nRespeite')[0]);
   assert.equal(data.pedido,nodes.request.value);assert.equal(data.projeto,nodes.target.value);assert.equal(data.estudo_anexado,true);
   assert(!nodes.output.value.includes('__CADU_TARGET__'));
  }
  await nodes.copy.events.click();assert.equal(clipboard,nodes.output.value);
  context.navigator.clipboard.writeText=async()=>{throw new Error('denied')};
  await nodes.copy.events.click();assert(nodes.output.selected);assert(nodes.status.textContent.includes('manualmente'));
  console.log('PASS: 10 modos, dados literais, cópia e fallback; DOM simulado, não navegador.');
 }catch(e){console.error(e);process.exitCode=1;}
});
