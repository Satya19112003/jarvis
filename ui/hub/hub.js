const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("hud") });
renderer.setSize(window.innerWidth, window.innerHeight);

const ring = new THREE.TorusGeometry(1, 0.03, 16, 100);
const material = new THREE.MeshBasicMaterial({ color: 0x00ffff });
const torus = new THREE.Mesh(ring, material);

scene.add(torus);
camera.position.z = 3;

function animate() {
  requestAnimationFrame(animate);
  torus.rotation.x += 0.01;
  torus.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();

