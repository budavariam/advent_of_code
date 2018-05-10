export function checkResult(solutionFunction: (_: string[]) => string, checkData: any, options?: any) {
    checkData.forEach((data: {input: string[], expected: string}, index: number) => {
        const calculated = solutionFunction(data.input);
        if (calculated === data.expected) {
            console.info("%d. Success", index);
        } else {
            console.error("%d. Failed", index);
            console.error(" calculated:", calculated);
            console.error(" expected:", data.expected);
        }
    });
}
