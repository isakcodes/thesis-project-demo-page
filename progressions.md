---
---

<h1>Sample Chordinator chord progressions</h1>
<p>Select a tab, then press play to listen.</p>
<div class="listening-area">
  <div class="tab">
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/163418_23_3_2024_generated_Blues.mid')">Blues</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/155747_23_3_2024_generated_Rock.mid')">Rock</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/160411_23_3_2024_generated_Jazz.mid')">Jazz 1</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/160810_23_3_2024_generated_Jazz.mid')">Jazz 2</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/161405_23_3_2024_generated_Jazz.mid')">Jazz 3</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/161602_23_3_2024_generated_Jazz.mid')">Jazz 4</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/161808_23_3_2024_generated_Jazz.mid')">Jazz 5</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/161915_23_3_2024_generated_Jazz.mid')">Jazz 6</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/162130_23_3_2024_generated_Jazz.mid')">Jazz 7</button>
    <button class="tablinks" onclick="openTab(event, 'assets/chordinator_samples/162708_23_3_2024_generated_Jazz.mid')">Jazz 8</button>
  </div>
  <div id="player">
    <midi-visualizer type="piano-roll" id="mainVisualizer" src=""></midi-visualizer>
    <midi-player src="" sound-font visualizer="#mainVisualizer" id="mainPlayer"></midi-player>
  </div>
</div>

{% raw %}
<script>
function openTab(evt, midiSrc) {
  var i, tablinks;
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  evt.currentTarget.className += " active";

  var midiVisualizer = document.getElementById('mainVisualizer');
  var midiPlayer = document.getElementById('mainPlayer');
  
  midiVisualizer.src = midiSrc;
  midiPlayer.src = midiSrc;
}
</script>
{% endraw %}