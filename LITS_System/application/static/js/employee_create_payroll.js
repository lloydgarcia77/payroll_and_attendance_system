$(document).ready(function() {

    function calculateTest2() {
        let basicPay = isNaN($("#basicPay").val()) == false ? $("#basicPay").val() : 0;
        let allowance = isNaN($("#allowance").val()) == false ? $("#allowance").val() : 0;
        let overtimePay = isNaN($("#overtimePay").val()) == false ? $("#overtimePay").val() : 0;
        let legalHoliday = isNaN($("#legalHoliday").val()) == false ? $("#legalHoliday").val() : 0;
        let sundaySpecialHoliday = isNaN($("#sundaySpecialHoliday").val()) == false ? $("#sundaySpecialHoliday").val() : 0;
        let lateAbsences = isNaN($("#basilateAbsencescPay").val()) == false ? $("#lateAbsences").val() : 0;
        let salaryCashAdvance = isNaN($("#salaryCashAdvance").val()) == false ? $("#salaryCashAdvance").val() : 0;

        let philhealContribution = isNaN($("#philhealContribution").val()) == false ? $("#philhealContribution").val() : 0;
        let pagibigContribution = isNaN($("#pagibigContribution").val()) == false ? $("#pagibigContribution").val() : 0;
        let sssPremius = 0;
        if ($("#cboSSS").prop("checked") == true) {
            sssPremius = isNaN($("#sssPremius").val()) == false ? $("#sssPremius").val() : 0;
        } else if ($("#cboSSS").prop("checked") == false) {
            sssPremius = 0;
        }

        let withholdingTax = isNaN($("#withholdingTax").val()) == false ? $("#withholdingTax").val() : 0;
        let pagibigLoan = isNaN($("#pagibigLoan").val()) == false ? $("#pagibigLoan").val() : 0;
        let deductionSalaryCashAdvance = isNaN($("#deductionSalaryCashAdvance").val()) == false ? $("#deductionSalaryCashAdvance").val() : 0;

        let gp = parseFloat(basicPay) + parseFloat(allowance) + parseFloat(overtimePay) + parseFloat(legalHoliday) + parseFloat(sundaySpecialHoliday) + parseFloat(salaryCashAdvance);
        let td = parseFloat(lateAbsences) + parseFloat(philhealContribution) + parseFloat(pagibigContribution) + parseFloat(sssPremius) + parseFloat(withholdingTax) + parseFloat(pagibigLoan) + parseFloat(deductionSalaryCashAdvance);
        let np = gp - td;
        console.log(gp);
        console.log(isNaN($("#philhealContribution").val()));
        console.log($("#philhealContribution").val() == "");
        $("#netPay").val(np);
    }

    function calculate() {
        let basicPay = $("#basicPay").val() == "" || isNaN($("#basicPay").val()) ? 0 : $("#basicPay").val();
        let allowance = $("#allowance").val() == "" || isNaN($("#allowance").val()) ? 0 : $("#allowance").val();
        let overtimePay = $("#overtimePay").val() == "" || isNaN($("#overtimePay").val()) ? 0 : $("#overtimePay").val();
        // let legalHoliday = $("#legalHoliday").val() == "" ? 0 : $("#legalHoliday").val();
        // let sundaySpecialHoliday = $("#sundaySpecialHoliday").val() == "" ? 0 : $("#sundaySpecialHoliday").val();
        let lateAbsences = $("#lateAbsences").val() == "" || isNaN($("#lateAbsences").val()) ? 0 : $("#lateAbsences").val();
        let salaryCashAdvance = $("#salaryCashAdvance").val() == "" || isNaN($("#salaryCashAdvance").val()) ? 0 : $("#salaryCashAdvance").val();
        //let grossPay = $("#grossPay").val() == null ? 0 : $("#grossPay").val();
        
        let sssPremius = 0;
        if ($("#cboSSS").prop("checked") == true) {
            sssPremius = $("#sssPremius").val() == "" || isNaN($("#sssPremius").val()) ? 0 : $("#sssPremius").val();
        } else if ($("#cboSSS").prop("checked") == false) { 
            sssPremius = 0;
        }
        let philhealContribution = 0;
        if ($("#cboPhilhealth").prop("checked") == true) {
            philhealContribution = $("#philhealContribution").val() == "" || isNaN($("#philhealContribution").val()) ? 0 : $("#philhealContribution").val();
        } else if ($("#cboPhilhealth").prop("checked") == false) { 
            philhealContribution = 0;
        }
        let pagibigContribution = 0;
        if ($("#cboPagibig").prop("checked") == true) {
            pagibigContribution = $("#pagibigContribution").val() == "" || isNaN($("#pagibigContribution").val()) ? 0 : $("#pagibigContribution").val();
        } else if ($("#cboPagibig").prop("checked") == false) { 
            pagibigContribution = 0;
        }

        let withholdingTax = $("#withholdingTax").val() == "" || isNaN($("#withholdingTax").val()) ? 0 : $("#withholdingTax").val();
        let pagibigLoan = $("#pagibigLoan").val() == "" || isNaN($("#pagibigLoan").val()) ? 0 : $("#pagibigLoan").val();
        let deductionSalaryCashAdvance = $("#deductionSalaryCashAdvance").val() == "" || isNaN($("#deductionSalaryCashAdvance").val()) ? 0 : $("#deductionSalaryCashAdvance").val();
        //let totalDeduction = $("#totalDeduction").val() == null ? 0 : $("#totalDeduction").val();

        // console.log(basicPay);
        // console.log(allowance);
        // console.log(overtimePay);
        // console.log(lateAbsences);
        // console.log(salaryCashAdvance);
        // console.log(philhealContribution);
        // console.log(pagibigContribution);
        // console.log(sssPremius);
        // console.log(withholdingTax);
        // console.log(pagibigLoan);
        // console.log(deductionSalaryCashAdvance);

        let gp = parseFloat(basicPay) + parseFloat(allowance) + parseFloat(overtimePay) + parseFloat(salaryCashAdvance);
        let td = parseFloat(lateAbsences) + parseFloat(philhealContribution) + parseFloat(pagibigContribution) + parseFloat(sssPremius) + parseFloat(withholdingTax) + parseFloat(pagibigLoan) + parseFloat(deductionSalaryCashAdvance);
        let np = gp - td;
        $("#grossPay").val(gp.toFixed(2));
        $("#totalDeduction").val(td.toFixed(2));
        $("#netPay").val(np.toFixed(2));
    }

    function calculateTest() {
        let basicPay = parseFloat($("#basicPay").val());
        let allowance = parseFloat($("#allowance").val());
        let overtimePay = parseFloat($("#overtimePay").val());
        let legalHoliday = parseFloat($("#legalHoliday").val());
        let sundaySpecialHoliday = parseFloat($("#sundaySpecialHoliday").val());
        let lateAbsences = parseFloat($("#basilateAbsencescPay").val());
        let salaryCashAdvance = parseFloat($("#salaryCashAdvance").val());
        let philhealContribution = parseFloat($("#philhealContribution").val());
        let pagibigContribution = parseFloat($("#pagibigContribution").val());
        let sssPremius = 0;
        if ($("#cboSSS").prop("checked") == true) {
            sssPremius = parseFloat($("#sssPremius").val());
        } else if ($("#cboSSS").prop("checked") == false) {
            sssPremius = 0;
        }

        let withholdingTax = parseFloat($("#withholdingTax").val());
        let pagibigLoan = parseFloat($("#pagibigLoan").val());
        let deductionSalaryCashAdvance = parseFloat($("#deductionSalaryCashAdvance").val());

        let gp = basicPay + allowance + overtimePay + parseFloat(legalHoliday) + parseFloat(sundaySpecialHoliday) + parseFloat(salaryCashAdvance);
        let td = parseFloat(lateAbsences) + parseFloat(philhealContribution) + parseFloat(pagibigContribution) + parseFloat(sssPremius) + parseFloat(withholdingTax) + parseFloat(pagibigLoan) + parseFloat(deductionSalaryCashAdvance);
        let np = gp - td;
        alert(np);
        $("#netPay").val(np);
    }
    $("#cboSSS, #cboPhilhealth, #cboPagibig").click(function() {
        calculate();
    });

    $("#salaryCashAdvance, #philhealContribution, #pagibigContribution, #withholdingTax, #pagibigLoan, #deductionSalaryCashAdvance").change(function() {
        calculate();
    });


});