const fs = require("fs");
const path = require("path");

const modulePackage = require.resolve("@paperclipai/server/package.json", {
  paths: [process.cwd()],
});
const assetsDir = path.join(path.dirname(modulePackage), "ui-dist", "assets");
const indexFileCandidates = fs
  .readdirSync(assetsDir, { withFileTypes: true })
  .filter((dirent) => dirent.isFile())
  .map((dirent) => dirent.name)
  .filter((name) => /^index-[A-Za-z0-9._-]+\.js$/.test(name))
  .sort();

if (indexFileCandidates.length === 0) {
  throw new Error("no Paperclip UI bundle found in ui-dist/assets");
}

const targetPath = path.join(
  assetsDir,
  indexFileCandidates[indexFileCandidates.length - 1]
);

const oldStr = 'const ht=(He??[]).find(Ye=>Ye.id===U),at=(te==null?void 0:te.checks.some(Ye=>Ye.code==="claude_anthropic_api_key_overrides_subscription"))??!1,nn=O==="claude_local"&&(te==null?void 0:te.status)==="fail"&&at,sn=y.useMemo(()=>{const Ye=T.trim().toLowerCase();return(He??[]).filter(ut=>{if(!Ye)return!0;const rn=cv(ut.id,"");return ut.id.toLowerCase().includes(Ye)||ut.label.toLowerCase().includes(Ye)||rn.toLowerCase().includes(Ye)})},[He,T]),dr=y.useMemo(()=>{if(O!=="opencode_local")return[{provider:"models",entries:[...sn].sort((ut,rn)=>ut.id.localeCompare(rn.id))}];const Ye=new Map;for(const ut of sn){const rn=cv(ut.id),Es=Ye.get(rn)??[];Es.push(ut),Ye.set(rn,Es)}return Array.from(Ye.entries()).sort(([ut],[rn])=>ut.localeCompare(rn)).map(([ut,rn])=>({provider:ut,entries:[...rn].sort((Es,cm)=>Es.id.localeCompare(cm.id))}))},[sn,O]);';

const newStr = 'const fr=y.useMemo(()=>{const Ye=[...(He??[])];return O==="codex_local"&&!Ye.some(ut=>ut.id===$y)&&Ye.unshift({id:$y,label:$y,provider:"openai"}),Ye},[He,O]),ht=fr.find(Ye=>Ye.id===U),at=(te==null?void 0:te.checks.some(Ye=>Ye.code==="claude_anthropic_api_key_overrides_subscription"))??!1,nn=O==="claude_local"&&(te==null?void 0:te.status)==="fail"&&at,sn=y.useMemo(()=>{const Ye=T.trim().toLowerCase();return fr.filter(ut=>{if(!Ye)return!0;const rn=cv(ut.id,"");return ut.id.toLowerCase().includes(Ye)||ut.label.toLowerCase().includes(Ye)||rn.toLowerCase().includes(Ye)})},[fr,T]),dr=y.useMemo(()=>{if(O!=="opencode_local")return[{provider:"models",entries:[...sn].sort((ut,rn)=>ut.id.localeCompare(rn.id))}];const Ye=new Map;for(const ut of sn){const rn=cv(ut.id),Es=Ye.get(rn)??[];Es.push(ut),Ye.set(rn,Es)}return Array.from(Ye.entries()).sort(([ut],[rn])=>ut.localeCompare(rn)).map(([ut,rn])=>({provider:ut,entries:[...rn].sort((Es,cm)=>Es.id.localeCompare(cm.id))}))},[sn,O]);';

const text = fs.readFileSync(targetPath, "utf8");

if (!text.includes(oldStr)) {
  throw new Error("Target pattern not found");
}

const updated = text.replace(oldStr, newStr);
fs.writeFileSync(targetPath, updated);

console.log(JSON.stringify({
  patched: true,
  hasNew: updated.includes("const fr=y.useMemo"),
  hasOld: updated.includes("const ht=(He??[]).find(Ye=>Ye.id===U)"),
  targetPath,
}));
