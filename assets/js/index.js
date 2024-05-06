import 'focus-visible';
import 'html-midi-player';
import {blobToNoteSequence} from '@magenta/music';

window.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('midiFile');
    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            blobToNoteSequence(e.target.files[0]).then((seq) => {
                document.getElementById('mainPlayer').noteSequence = seq;
                document.getElementById('mainVisualizer').noteSequence = seq;
            }).catch((reason) => {
                alert('Failed to load MIDI file.');
                console.error(reason);
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', (event) => {
  var moonIcon = document.getElementById('moonIcon');
  var sunIcon = document.getElementById('sunIcon');
  var isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

  // Set initial icon state
  if (isDarkMode) {
    moonIcon.style.display = 'none';
    sunIcon.style.display = 'inline-block';
  } else {
    moonIcon.style.display = 'inline-block';
    sunIcon.style.display = 'none';
  }

  document.getElementById('darkModeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    document.body.classList.add('manual-dark-mode');
    if (document.body.classList.contains('dark-mode')) {
      moonIcon.style.display = 'none';
      sunIcon.style.display = 'inline-block';
    } else {
      moonIcon.style.display = 'inline-block';
      sunIcon.style.display = 'none';
    }
  });
});