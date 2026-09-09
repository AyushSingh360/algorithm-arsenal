/**
 * Target Cursor Animation
 * A sleek, trailing cursor effect drawn on a fixed canvas.
 */
(function () {
  'use strict';

  // Only run on desktop devices
  if (window.matchMedia('(max-width: 768px)').matches || ('ontouchstart' in window)) return;

  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100vw';
  canvas.style.height = '100vh';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '9999';
  
  document.body.appendChild(canvas);

  let width = window.innerWidth;
  let height = window.innerHeight;
  canvas.width = width;
  canvas.height = height;

  window.addEventListener('resize', () => {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
  });

  const mouse = { x: width / 2, y: height / 2 };
  const target = { x: width / 2, y: height / 2, radius: 15 };
  const dot = { x: width / 2, y: height / 2, radius: 3 };
  let isMoving = false;
  let timer = null;

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    isMoving = true;
    
    clearTimeout(timer);
    timer = setTimeout(() => {
      isMoving = false;
    }, 100);
  });

  function lerp(start, end, amt) {
    return (1 - amt) * start + amt * end;
  }

  function render() {
    ctx.clearRect(0, 0, width, height);
    
    const theme = document.documentElement.getAttribute('data-theme') || 'dark';
    const color = theme === 'dark' ? 'rgba(255, 255, 255, 0.8)' : 'rgba(0, 0, 0, 0.8)';
    const ringColor = theme === 'dark' ? 'rgba(100, 200, 255, 0.5)' : 'rgba(0, 100, 200, 0.4)';

    // Lerp dot to mouse fast
    dot.x = lerp(dot.x, mouse.x, 0.4);
    dot.y = lerp(dot.y, mouse.y, 0.4);

    // Lerp target to mouse slowly
    target.x = lerp(target.x, mouse.x, 0.15);
    target.y = lerp(target.y, mouse.y, 0.15);

    // Expand radius slightly when moving
    const targetRadius = isMoving ? 25 : 15;
    target.radius = lerp(target.radius, targetRadius, 0.1);

    // Draw outer target ring
    ctx.beginPath();
    ctx.arc(target.x, target.y, target.radius, 0, Math.PI * 2);
    ctx.strokeStyle = ringColor;
    ctx.lineWidth = 1.5;
    ctx.stroke();
    
    // Draw crosshairs
    const d = target.radius + 4;
    ctx.beginPath();
    ctx.moveTo(target.x, target.y - d);
    ctx.lineTo(target.x, target.y - target.radius + 2);
    ctx.moveTo(target.x, target.y + target.radius - 2);
    ctx.lineTo(target.x, target.y + d);
    ctx.moveTo(target.x - d, target.y);
    ctx.lineTo(target.x - target.radius + 2, target.y);
    ctx.moveTo(target.x + target.radius - 2, target.y);
    ctx.lineTo(target.x + d, target.y);
    ctx.strokeStyle = ringColor;
    ctx.stroke();

    // Draw inner dot
    ctx.beginPath();
    ctx.arc(dot.x, dot.y, dot.radius, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();

    requestAnimationFrame(render);
  }

  render();
})();
