document.getElementById("prediction-form").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent form submission

    const formData = {
        query: `
            mutation {
                predict(
                    firstTermGpa: ${document.getElementById('first_term_gpa').value},
                    secondTermGpa: ${document.getElementById('second_term_gpa').value},  
                    firstLanguage: ${document.getElementById('first_language').value},
                    funding: ${document.getElementById('funding').value},
                    fastTrack: ${document.getElementById('fast_track').value},
                    coop: ${document.getElementById('coop').value},
                    residency: ${document.getElementById('residency').value},
                    gender: ${document.getElementById('gender').value},
                    prevEducation: ${document.getElementById('prev_education').value},
                    ageGroup: ${document.getElementById('age_group').value},
                    mathScore: ${document.getElementById('math_score').value},
                    englishGrade: ${document.getElementById('english_grade').value}
                ) {
                    result
                }
            }
        `
    };

    try {
        // Send the GraphQL request
        const response = await fetch("/graphql", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        const prediction = result.data.predict.result;

        // Display the result
        document.getElementById("result").innerText = `According to your input values, the predicted student's first year persitance is : ${prediction}`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Failed to get prediction.";
    }
});