from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
start = s.index('const ALLOWED_EMAIL_HASHES=')
end = s.index('</script>', start)
new = r'''const USERS={"b6a6b14c521fe88f50ab6de404741e5b544393a234c1f5b91798a192b1d58fb2":{"s":"oiEdB0R8A0M6aikA/hVf9g==","m":"LhYaM27H8gKqHArq4GthMRX7HtMZ8bB41wYYNgfRNgw="},"d4dcb3c9dc57ad54e9a8e11b3b1a67e793505b298d91308a28f966f449703417":{"s":"TU+kowirfA4yVSAcfy5TfA==","m":"dK7JLb71irAEBFAEUbgaWouBgDDfQrk/B49FuwQBYXY="},"26df5e785526ad92179f306225a98891d1aff08f321ac576a4b11738697a6540":{"s":"0QuDR94rsy3Spgpe98e3lw==","m":"1we+f5vWhts7bxHA68e3aJwnal3PgAkYWncbSEJo3xI="},"672e32f622afc306b2472ef88c945086e1c0d2ed1fe084ee15390d0cdddb7c8d":{"s":"9zjc8RYW6mgeGCu3wQxBCQ==","m":"Fw+RrwK2Nrmh0CsjFXc3WKap2MyEV9/ndAwWP0jrWVY="}};
async function H(v){const n=v.trim().toLowerCase(),h=await crypto.subtle.digest("SHA-256",te.encode(n));return [...new Uint8Array(h)].map(x=>x.toString(16).padStart(2,"0")).join("");}
async function d(c,u){let x=await crypto.subtle.importKey("raw",te.encode(c.trim().toUpperCase()),"PBKDF2",false,["deriveBits"]),bits=new Uint8Array(await crypto.subtle.deriveBits({name:"PBKDF2",salt:b(u.s),iterations:N,hash:"SHA-256"},x,256)),mask=b(u.m),raw=new Uint8Array(32);for(let i=0;i<32;i++)raw[i]=bits[i]^mask[i];return crypto.subtle.importKey("raw",raw,"AES-GCM",true,["decrypt"]);}
async function z(u){const ds=new DecompressionStream("gzip"),w=ds.writable.getWriter();w.write(u);w.close();return td.decode(await new Response(ds.readable).arrayBuffer());}
async function e(k,m){let p=await crypto.subtle.decrypt({name:"AES-GCM",iv:b(I),additionalData:b(A)},k,b(C)),h=await z(new Uint8Array(p));localStorage.setItem("immex_lef_pilot_key",B(await crypto.subtle.exportKey("raw",k)));if(m)localStorage.setItem("immex_lef_pilot_identity",m);document.open();document.write(h);document.close();}
(async()=>{let s=localStorage.getItem("immex_lef_pilot_key");if(s)try{let k=await crypto.subtle.importKey("raw",b(s),"AES-GCM",true,["decrypt"]);await e(k,localStorage.getItem("immex_lef_pilot_identity")||"")}catch(_){localStorage.removeItem("immex_lef_pilot_key")}})();
gate.onsubmit=async q=>{q.preventDefault();btn.disabled=true;msg.textContent="Έλεγχος πρόσβασης…";const identity=email.value.trim(),h=await H(identity),u=USERS[h];if(!u){msg.textContent="Το email δεν είναι εγκεκριμένο για πρόσβαση.";btn.disabled=false;return}try{await e(await d(code.value,u),identity)}catch(_){msg.textContent="Λανθασμένος προσωπικός κωδικός πρόσβασης.";btn.disabled=false}};
'''
s = s[:start] + new + s[end:]
s = s.replace('placeholder="Lef01-XXXX"', 'placeholder="Προσωπικός κωδικός"')
s = s.replace('Pilot στάδιο: πρόσβαση μόνο σε εγκεκριμένα emails + pilot code. Αν εγκριθεί, το production στάδιο θα χρησιμοποιεί one-time email OTP.', 'Pilot στάδιο: πρόσβαση μόνο σε εγκεκριμένα emails. Κάθε χρήστης έχει προσωπικό κωδικό. Αν εγκριθεί, το production στάδιο θα χρησιμοποιεί one-time email OTP.')
p.write_text(s, encoding='utf-8')
