function openTab(evt, tabName) {
    var i, tablinks;
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    evt.currentTarget.className += " active";

    var midiVisualizer = document.getElementById('mainVisualizer');
    var midiPlayer = document.getElementById('mainPlayer');

    if (tabName === 'Example1') {
        midiVisualizer.src = 'tmp4lx38tfj.mid';
        midiPlayer.src = 'tmp4lx38tfj.mid';
    } else if (tabName === 'Example2') {
        midiVisualizer.src = 'example2.mid';
        midiPlayer.src = 'example2.mid';
    }
}