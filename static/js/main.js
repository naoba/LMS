function AgetoDOB(){
    var age = document.getElementById("age").value
    age = age.trim();
    if (age.length != 0){
        const date = new Date();
        const yy = date.getFullYear();
        const mm = String(date.getMonth() + 1).padStart(2, '0');
        const dd = String(date.getDate()).padStart(2, '0');
    
        var dobYear = yy - age;
        const newdob = [dobYear, mm, dd].join('-');

        var dob = document.getElementById("id_dob")
        dob.value = newdob
        }
    else{
        alert("Age Not Be Empty")
        } 
}

function DOBtoAge(){
    var dob = document.getElementById("id_dob").value

    dob = new Date(dob);
    const today = new Date();
    let ageYears = today.getFullYear() - dob.getFullYear();
    let ageMonths = today.getMonth() - dob.getMonth();
    let ageDays = today.getDate() - dob.getDate();

    // Adjust for negative months or days
    if (ageDays < 0) {
        const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1, birth.getDate());
        ageDays = Math.floor((today - lastMonth) / (1000 * 60 * 60 * 24));
    }

    if (ageMonths < 0) {
        ageMonths += 12;
        ageYears--;
    }
    const age = [ageYears+'Y', ageMonths+'M', ageDays+'D'].join(' ');

    document.getElementById("age").value = age; 
    document.getElementById('age').setAttribute("disabled", "True");
    
    // console.log(age)

}

// function FilePath(){
//     var path = document.getElementById("json_to_excel").files[0];
//     alert(path);

// }
$('input[type=file]').change(function () {
    console.log(this.files[0].mozFullPath);
});
