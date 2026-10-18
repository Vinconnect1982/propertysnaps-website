(()=>{
  'use strict';
  const menu=document.querySelector('.menu-toggle');
  const nav=document.getElementById('nav');
  if(menu&&nav){
    const setMenu=(open,restoreFocus=false)=>{
      nav.classList.toggle('open',open);
      menu.setAttribute('aria-expanded',String(open));
      menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');
      if(!open&&restoreFocus)menu.focus();
    };
    menu.addEventListener('click',()=>setMenu(!nav.classList.contains('open')));
    nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>setMenu(false)));
    document.addEventListener('keydown',event=>{
      if(event.key==='Escape'&&nav.classList.contains('open'))setMenu(false,true);
    });
    document.addEventListener('click',event=>{
      if(nav.classList.contains('open')&&!nav.contains(event.target)&&!menu.contains(event.target))setMenu(false);
    });
    window.addEventListener('resize',()=>{if(window.innerWidth>840&&nav.classList.contains('open'))setMenu(false)});
  }

  const filters=[...document.querySelectorAll('[data-filter]')];
  const grid=document.getElementById('gallery');
  const cards=grid?[...grid.querySelectorAll('.gallery-item[data-cat]')]:[];
  if(filters.length&&grid){
    const count=document.createElement('p');
    count.className='filter-summary';
    count.setAttribute('role','status');
    count.setAttribute('aria-live','polite');
    document.querySelector('.filterbar')?.after(count);
    const applyFilter=(category)=>{
      filters.forEach(button=>{
        const active=button.dataset.filter===category;
        button.classList.toggle('active',active);
        button.setAttribute('aria-pressed',String(active));
      });
      cards.forEach(card=>{card.hidden=category!=='All'&&card.dataset.cat!==category});
      const visible=cards.filter(card=>!card.hidden).length;
      count.textContent=`Showing ${visible} ${visible===1?'image':'images'}${category==='All'?'':` in ${category}`}.`;
    };
    filters.forEach(button=>button.addEventListener('click',()=>applyFilter(button.dataset.filter)));
    applyFilter(filters.find(button=>button.classList.contains('active'))?.dataset.filter||'All');
  }

  if(grid&&typeof HTMLDialogElement!=='undefined'){
    const dialog=document.createElement('dialog');
    dialog.className='lightbox';
    dialog.setAttribute('aria-label','Enlarged portfolio photograph');
    dialog.innerHTML=`<button class="lightbox-close" type="button" aria-label="Close image">×</button>
      <button class="lightbox-prev" type="button" aria-label="Previous photograph">‹</button>
      <figure><img alt=""><figcaption class="lightbox-caption"></figcaption></figure>
      <button class="lightbox-next" type="button" aria-label="Next photograph">›</button>`;
    document.body.append(dialog);
    let visibleCards=[],activeIndex=0,returnFocus=null;
    const display=(index)=>{
      if(!visibleCards.length)return;
      activeIndex=(index+visibleCards.length)%visibleCards.length;
      const card=visibleCards[activeIndex];
      const img=card.querySelector('img');
      const large=dialog.querySelector('img');
      large.src=img.currentSrc||img.src;
      large.alt=img.alt||'Property portfolio image';
      dialog.querySelector('.lightbox-caption').textContent=`${card.querySelector('figcaption strong')?.textContent||large.alt} · ${activeIndex+1} of ${visibleCards.length}`;
    };
    grid.querySelectorAll('.gallery-item').forEach(card=>card.addEventListener('click',event=>{
      event.preventDefault();
      visibleCards=cards.filter(item=>!item.hidden);
      if(!visibleCards.includes(card))return;
      returnFocus=card;
      display(visibleCards.indexOf(card));
      dialog.showModal();
      dialog.querySelector('.lightbox-close').focus();
    }));
    dialog.querySelector('.lightbox-close').addEventListener('click',()=>dialog.close());
    dialog.querySelector('.lightbox-prev').addEventListener('click',()=>display(activeIndex-1));
    dialog.querySelector('.lightbox-next').addEventListener('click',()=>display(activeIndex+1));
    dialog.addEventListener('keydown',event=>{
      if(event.key==='ArrowRight'){event.preventDefault();display(activeIndex+1)}
      if(event.key==='ArrowLeft'){event.preventDefault();display(activeIndex-1)}
    });
    dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close()});
    dialog.addEventListener('close',()=>{returnFocus?.focus();returnFocus=null});
  }
})();
