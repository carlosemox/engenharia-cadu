const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'docs/fabrica/routes.json'),'utf8'));
const nodes={};
for(const id of ['status','mode','target','request','attachment','output','copy','repository','checkout','branch','code-revision','requirement','state','environment','services','authorizations','blockers','stop-requested'])nodes[id]={value:'',textContent:'',checked:false,events:{},addEventListener(e,f){this.events[e]=f},focus(){},select(){this.selected=true}};
nodes.mode.value='auto';let clipboard='';
const context={document:{getElementById:id=>nodes[id], querySelectorAll:()=>[]},fetch:async()=>({ok:true,json:async()=>catalog}),navigator:{clipboard:{writeText:async text=>{clipboard=text}}}};
vm.runInNewContext(fs.readFileSync(path.join(root,'docs/assets/factory.js'),'utf8'),context);
setImmediate(async()=>{
 try{
  assert.equal(nodes.status.textContent,''); assert(nodes.output.value.includes('CADU'));
  nodes.target.value='repo "x" <script>no()</script>';
  nodes.request.value="Preservar $& $$ $` $'\ntexto";nodes.attachment.checked=true;
  for(const mode of Object.keys(catalog.routes)){
   nodes.mode.value=mode;nodes.mode.events.input();
   const data=JSON.parse(nodes.output.value.split('adicional):\n')[1]);
   assert.equal(data.pedido,nodes.request.value);assert.equal(data.projeto,nodes.target.value);assert.equal(data.estudo_anexado,true);
   assert(!nodes.output.value.includes('__CADU_TARGET__'));
  }
  nodes.repository.value='carlosemox/engenharia-cadu';
  nodes.requirement.value='REQ-001: publicação tri-língue';
  nodes['stop-requested'].value='requested';
  nodes.repository.events.input();
  const enriched=JSON.parse(nodes.output.value.split('adicional):\n')[1]);
  assert.equal(enriched.repositorio,'carlosemox/engenharia-cadu');
  assert.equal(enriched.requisito_aprovado,'REQ-001: publicação tri-língue');
  assert.equal(enriched.stop_requested,true);
  await nodes.copy.events.click();assert.equal(clipboard,nodes.output.value);
  context.navigator.clipboard.writeText=async()=>{throw new Error('denied')};
  await nodes.copy.events.click();assert(nodes.output.selected);assert(nodes.status.textContent.includes('manualmente'));
  console.log(`PASS: ${Object.keys(catalog.routes).length} modos, dados literais, cópia e fallback; DOM simulado, não navegador.`);
 }catch(e){console.error(e);process.exitCode=1;}
});
