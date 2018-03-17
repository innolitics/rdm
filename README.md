# Regulatory Documentation Manager

## Philosophy

Some students go to school because they need the degree to get a job.  These students optimize their actions to get the best grades for the least amount of work.

The best students go to school to learn, and while they often try to get good grades, they optimize their actions so as to learn as much as they can.

Likewise, some companies follow regulations to get certified to sell their products.  They optimize everything they do to get past the regulators for the lowest cost.

The best companies follow the regulations with a degree of faith that these regulations will make their products better and safer.

## Introduction

Our Regulatory Documentation Manager (RDM) is a set of templates and python scripts for streamlining the process of complying with the IEC62304 standard.  We believe that IEC62304 is a good standard, and that it makes our software better and safer for for the medical practioners and patients that interact with our client's software.

RDM is designed to be used by software developers.

Many companies have other employees manage their regulatory documentation because the time costs are too high to have software developers manage the regulatory documentation directly.  We believe that software developers are in the best position to handle most of the tasks required by IEC62304.  Furthermore, this tool streamlines the many regulatory tasks by integrating it tightly into software development workflow.

## References

References to IEC62304:2006 are indicate in square brackets throughout the RDM documentation.  For example, `[5.1.9]` refers to section 5.1.9 of the IEC62304:2006 standard.

## Medical Devices with vs. without Hardware Components

RDM is designed to work well for medical devices with and without hardware components.

Medical devices that contain a hardware component must comply with a larger body of standards, for example IEC60601-1.  When this is the case, the _software requirements_ must be tied to the larger _system requirements_.

RDM works well with "software only devices" (also known as Software as a Medical Device, SaMD).  In this case, the _software requirements_ and _system requirements_ are equivalent [5.2.1].
