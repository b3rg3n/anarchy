function vexHuetaUved(text) {
    vex.dialog.alert({
        message: text,
    })
}

function vexHuetaTranslates() {
    vex.dialog.alert({
        message: 'Мы много переводов сделали. Тебе какой нужен?\n\nЕсть Her Story, и прочее говно.',
    })
}

const mishlent = {
    isGay: false,
    authorOfSkeetRemaster: true,
    srDownload: function () {
        console.log('Потом скачаешь, заебал')
    }
}

mishlent.srDownload()